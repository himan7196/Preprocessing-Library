import base
import pandas as pd

dataset = pd.read_csv('Data.csv')

X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 4:5].values

base.Configuration.numerical_data_configuration(base.Configuration, feature_scaling=True, handle_null= True,)
base.Configuration.text_data_configuration(base.Configuration, only_alpha=True, stem=True, stopword_removal=True)

print(X)

X = base.Text.lemmetization(base.Text, X, 3)


print('\n\n\n\n')

print(X)


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
