import base
import pandas as pd

dataset = pd.read_csv('datasets\Data.csv')

X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 4].values

base.Configuration.numerical_data_configuration(base.Configuration, handle_null=True)



#Specify the column number of your dataframe in a list
X = base.Numeric.handle_null(base.Numeric, X, 1,2)




'''
c = base.Configuration.text_data_configuration(base.Configuration)
text = 'Keeping goes going go went kept keep playing plays the is this the'

#text = base.Text.stemming(base.Text, text)
print(text)

#c2 = base.Configuration.numerical_data_configuration(base.Configuration, feature_scaling=True, handle_null=True)
text = base.Text(text)
number = base.Numeric()
'''
