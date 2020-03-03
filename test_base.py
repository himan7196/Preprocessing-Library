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
    
    return numeric_columns,text_columns

numeric_columns, text_columns = validate_columns(numeric_columns, text_columns)

if not output_file_name:
    output_file_name = 'processed'


print(numeric_columns, text_columns)



X = dataset.iloc[:, :].values

base.Numeric(feature_scaling=config["feature_scaling"], handle_null=config["handle_null"], data=X, columns=numeric_columns)
base.Text(only_alpha=config["only_alpha"], stem=config["stem"], lemma=config["lemma"], stopword_removal=["stopword_removal"], handle_null=["handle_null_text"], data=X, columns=text_columns)

'''feather.write_dataframe(dataset, output_file_name+'.feather')

z = pd.read_feather(output_file_name+'.feather')'''

'''with open(output_file_name, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headings)
    writer.writerows(X)'''

dataframe = pd.DataFrame(data=X[:,:], columns=headings)

feather.write_dataframe(dataframe, output_file_name)
print(dataframe)


'''
#Specify the column number of your dataframe in a list

print('X before: ', X)

X = base.Numeric.feature_scaling(base.Numeric, X, 1, 2)
X = base.Numeric.handle_null(base.Numeric, X, 1,2)
print('X after: ', X)
#X = base.Numeric.handle_null(base.Numeric, X, 1,2)
'''



'''
c = base.Configuration.text_data_configuration(base.Configuration)
text = 'Keeping goes going go went kept keep playing plays the is this the'

#text = base.Text.stemming(base.Text, text)
print(text)

#c2 = base.Configuration.numerical_data_configuration(base.Configuration, feature_scaling=True, handle_null=True)
text = base.Text(text)
number = base.Numeric()
'''
