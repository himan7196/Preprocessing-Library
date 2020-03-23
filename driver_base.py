import base
import pandas as pd
import json
import csv
import feather
import dask.array as da
import dask.dataframe as df
import dask_ml

'''format = "%(name)s - %(process)d - %(asctime)s -%(levelname)s - %(message)s"
logger = logging.getLogger('Logger')
logger.setLevel(logging.INFO)
format = logging.Formatter(format)
handler = RotatingFileHandler(filename= "logs\\ppl_report.log", maxBytes=4096, backupCount=5)
handler.setFormatter(format)
logger.addHandler(handler)'''

base.logger.info('Script initiated')
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
base.logger.info('Reading input from: '+input_file_path)


dataset = pd.read_csv(input_file_path)
dataset_dask = df.read_csv(input_file_path)


headings = [item for item in dataset.columns]


def validate_columns(numeric_columns, text_columns, category_columns):
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
    else:
        temp_list = []
        total_list = []
        for i in range (len(headings)):
            if dataset.dtypes[headings[i]]==object or dataset.dtypes[headings[i]]==str:
                total_list.append(i)
                temp = dataset.iloc[:,i].values
                num_tokens = config["max_token_limit"]
                row_counter_limit = config["max_row_limit"]
                row_counter = 0
                for item in temp:
                    tokens = item.split(' ')
                    if len(tokens)>num_tokens:
                        row_counter+=1
                        if row_counter>row_counter_limit:
                            temp_list.append(i)
                            break
            elif dataset.dtypes[headings[i]]==float or dataset.dtypes[headings[i]]==int:
                total_list.append(i)
                temp = dataset.iloc[:,i].values
                set_of_temp = set(temp)
                max_cat_for_num = config["max_cat_for_num"]
                if len(set_of_temp)>max_cat_for_num:
                    temp_list.append(i)

        category_columns = list(set(total_list)-set(temp_list))
        for item in category_columns:
            if item in numeric_columns:
                numeric_columns.remove(item)
            if item in text_columns:
                text_columns.remove(item)
    
    return numeric_columns, text_columns, category_columns, 1

numeric_columns, text_columns, category_columns, code = validate_columns(numeric_columns, text_columns, category_columns)

temp_string = ''
for item in numeric_columns:
    temp_string += str(headings[item])+f'({item}), '
base.logger.info('Numeric columns in the dataset: '+temp_string)
temp_string = ''
for item in text_columns:
    temp_string += str(headings[item])+f'({item}), '
base.logger.info('Text columns in the dataset: '+temp_string)
temp_string = ''
for item in category_columns:
    temp_string += str(headings[item])+f'({item}), '
base.logger.info('Category column in the dataset: '+temp_string)


if not output_file_name:
    output_file_name = '..\\files\\processed\\processed'
else:
    output_file_name = '..\\files\\processed\\'+output_file_name



X = dataset.iloc[:, :].values
X_dask = dataset_dask.iloc[:,:].values

base.logger.info('Calling the method for numeric data')
base.Numeric(feature_scaling=config["feature_scaling"], handle_null=config["handle_null"], handle_null_strategy= config["handle_null_strategy"], data=X, columns=numeric_columns)
base.logger.info('Calling the method for text data')
base.Text(only_alpha=config["only_alpha"], stem=config["stem"], lemma=config["lemma"], stopword_removal=config["stopword_removal"], count_vect = config["count_vect"], data=X, columns=text_columns)
base.logger.info('Calling the method for categorical data')
base.Categorical(label_encoding = config["label_encoding"], data=X, columns=category_columns)

#Writing to feather
dataframe = pd.DataFrame(data=X[:,:], columns=headings)
feather.write_dataframe(dataframe, output_file_name)
base.logger.info('Feather file written')


base.logger.info('Script ended. Output directory: '+output_file_name+'\n\n')

#new = pd.read_feather(output_file_name)
#print(new.iloc[:,:].values)


#Writing to csv
'''with open(output_file_name, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headings)
    writer.writerows(X)
'''
