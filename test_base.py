import base
import pandas as pd
import json
import csv
import feather

def read_config(file_path):
    with open(file_path) as f:
        config = json.load(f)
    return config
config = read_config('configuration.json')


input_file_path = config["input_file_path"]
numeric_columns = config["numeric_columns"]
text_columns = config["text_columns"]
category_columns = config["category_columns"]
output_file_name = config["output_file_name"]


dataset = pd.read_csv(input_file_path)
headings = [item for item in dataset.columns]

def validate_columns(numeric_columns, text_columns):
    if numeric_columns:
        for i in range(len(numeric_columns)):
            numeric_columns[i] = int(numeric_columns[i])
    else:
        numeric_columns = []  
        for i in range (len(headings)):
            if dataset.dtypes[headings[i]]==float or dataset.dtypes[headings[i]]==int:
                numeric_columns.append(i)

    if text_columns:
        for i in range(len(text_columns)):
            text_columns[i] = int(text_columns[i])
    else:
        text_columns = []
        for i in range (len(headings)):
            if dataset.dtypes[headings[i]]==object or dataset.dtypes[headings[i]]==str:
                text_columns.append(i)

    if category_columns:
        for i in range(len(category_columns)):
            category_columns[i] = int(category_columns[i]) 
    
    return numeric_columns,text_columns

numeric_columns, text_columns = validate_columns(numeric_columns, text_columns)

if not output_file_name:
    output_file_name = 'processed'




X = dataset.iloc[:, :].values

base.Numeric(feature_scaling=config["feature_scaling"], handle_null=config["handle_null"], data=X, columns=numeric_columns)
#base.Text(only_alpha=config["only_alpha"], stem=config["stem"], lemma=config["lemma"], stopword_removal=["stopword_removal"], data=X, columns=text_columns)
base.Categorical(label_encoding=config["label_encoding"], one_hot_encoding=config["one_hot_encoding"], data=X, columns=category_columns)


print(X)
#Writing to feather
dataframe = pd.DataFrame(data=X[:,:], columns=headings)
feather.write_dataframe(dataframe, output_file_name)


#Writing to csv
'''with open(output_file_name, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headings)
    writer.writerows(X)
'''
