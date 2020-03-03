# PREPROCESS
Currently this supports below functionalities. Assign the values in the *configuration.json* file

## BASIC CONFIGURATION

- **Input file path and output file name**
```json
    {
        "input_file_path": "source",
        "output_file_name": "filename"
    }
```
- **Column numbers for specific data type**
```json
    {
        "numeric_columns": ["1"],
        "text_columns": ["2"],
        "category_columns": ["3","4"] 
    }
```

## NUMERICAL
- **Feature Scaling** : 
```json
    {
        "feature_scaling": true
    }
```
- **Null Handing** :

```json
    {
        "handle_null": true
    }
```

## TEXT
- **English alphabets only** : 
```json
    {
        "only_alpha": true
    }
```
- **Stemming** :

```json
    {
        "stem": true
    }
```

- **Lemmatization** :

```json
    {
        "lemma": true
    }
```

- **Stopwords removal** :

```json
    {
        "stopwords_removal": true
    }
```

 
## CATEGORICAL
- **Encoding** :

```json
    {
        "encoding": true
    }
```

## SPEECH
## IMAGE
## MIXED