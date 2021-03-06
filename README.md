# PREPROCESSING-LIBRARY
Currently this supports below functionalities. Assign the values in the *configuration.json* file

## BASIC CONFIGURATION

- **Input file path and output file name** : 
Expects a *string* type input.
Default:
    *output_file_name* = "processed"
```json
    {
        "input_file_path": "source",
        "output_file_name": "filename"
    }
```
- **Column numbers for specific data type** : 
Expects *list* based inputs. In case of null, action will be performed on all the columns of specific types.
```json
    {
        "numeric_columns": ["1"],
        "text_columns": "",
        "category_columns": ["3","4"] 
    }
```

- **Limit for categorical classification** : 
Expects *integer* type values. Automatically classify the data type if no value provided in the column number section. 
```json
    {
        "max_cat_for_num": 3,
        "max_token_limit": 5,
        "max_row_limit": 3, 
    }
```
*max_cat_for_num* : maximum number of categories allowed for numeric type.
*max_token_limit* : maximum number of tokens for a row.
*max_row_limit* : maximum number of rows for the threshold.

*eg.* 
- for *max_token_limit* =5, *max_row_limit* =3, if 3 or more rows are found to be containing 5 or more tokens, it will not be considered as categorical type.

- for *max_cat_for_num* =3, if any numeric column has more than 3 distinct values, it will not be considered as categorical type.


## NUMERICAL
- **Feature Scaling** : 
Expects a *boolean* type input.
```json
    {
        "feature_scaling": true
    }
```
- **Null Handing** :
Expects a *boolean* type input and a value *mean/median/most_frequent*
```json
    {
        "handle_null": true,
        "handle_null_strategy": "mean"
    }
```

## TEXT
- **English alphabets only** : 
Expects a *boolean* type input.
```json
    {
        "only_alpha": true
    }
```
- **Stemming** :
Expects a *boolean* type input.
```json
    {
        "stem": true
    }
```

- **Lemmatization** :
Expects a *boolean* type input.
```json
    {
        "lemma": true
    }
```

- **Stopwords removal** :
Expects a *boolean* type input.
```json
    {
        "stopwords_removal": true
    }
```

- **Count Vectorizer** :
```
    Currently it stores the count vectors of specified columns in a list that is a Text class object. Needs to be modified.
```
Expects a *boolean* type input.
```json
    {
        "count_vect": true
    }
```
 
## CATEGORICAL
- **Encoding** :
Expects a *boolean* type input.
```json
    {
        "label_encoding": true
    }
```

## SPEECH
## IMAGE
## MIXED