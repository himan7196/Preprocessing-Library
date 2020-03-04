'''Add the name of the package you want to use in the file'''
import numpy
import nltk
import re
import sklearn
import numpy
import nltk
import regex
import logging
    
from nltk.tokenize.toktok import ToktokTokenizer
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.compose import ColumnTransformer
from logging.handlers import RotatingFileHandler
# Download the required data
# nltk.download('stopwords')
# nltk.download('wordnet')


format = "%(name)s - %(process)d - %(asctime)s -%(levelname)s - %(message)s"
logger = logging.getLogger("Logger")
logger.setLevel(logging.INFO)
format = logging.Formatter(format)
handler = RotatingFileHandler(filename = "logs\\log_report.log", mode='w', maxBytes=4096 , backupCount=5)
handler.setFormatter(format)
logger.addHandler(handler)

class Categorical:
    def __init__(self, label_encoding, data, columns):
        logger.info('Categorical class instantiated')
        if label_encoding == True:
            logger.info('Launching the label encoder method')
            self.label_encoding(data, columns)


    def label_encoding(self, data, columns):
        for item in columns:
            lab_enc = LabelEncoder()
            data[:, item] = lab_enc.fit_transform(data[:, item])
            logger.info('Label encoding success')
        return data
            



class Numeric():
    def __init__(self, feature_scaling, handle_null, handle_null_strategy, data, columns):
        logger.info('Numerical class instantiated')
        if handle_null == True:
            logger.info(f'Launching the null handler with stratgey: {handle_null_strategy}')
            self.handle_null(data, handle_null_strategy, columns)
        if feature_scaling == True:
            logger.info('Launching the feature scaling')
            self.feature_scaling(data, columns)


    def feature_scaling(self, data, columns):
        sc = StandardScaler()
        for item in columns:
            data[:, item:item+1] = sc.fit_transform(data[:, item:item+1])
        logger.info('Feature scaling success')
        return data
        

    
    #Currently replacing the NaN by mean
    def handle_null(self, data, handle_null_strategy, columns):
        imputer = SimpleImputer(missing_values = numpy.nan, strategy = handle_null_strategy)
        for item in columns:
            item = int(item)
            imputer = imputer.fit(data[:,item:item+1])
            data[:,item:item+1] = imputer.transform(data[:,item:item+1])
        logger.info('Null handling success')
        return data
        


class Text ():
    def __init__(self, only_alpha, stem, lemma, stopword_removal, data, columns):
        logger.info('Text class instantiated')
        if only_alpha==True:
            logger.info('Launching the only alpahbets')
            self.only_alphabets(data, columns)
        if stem==True:
            logger.info('Launching the stemming')
            self.stemming(data, columns)
        if lemma==True:
            logger.info('Launching the lemmetization')
            self.lemmetization(data, columns)
        if stopword_removal==True:
            logger.info('Launching the stopwords removal')
            self.stopword_removal(data, columns)
        

    def only_alphabets(self, data, columns):
        '''How to handle nltk.download('stopwords')'''
        for item in columns:
            for i in range (len(data)):
                text = re.sub('[^a-zA-Z]', ' ', str(data[i:i+1,item:item+1]))
                text = re.sub(' +', ' ', text)
                text = text.lower()
                #text = text.split()
                #ps = PorterStemmer()
                #text = [ps.stem(word) for word in text if not word in set(stopwords.words('english'))]
                #text = ' '.join(text)
                data[i:i+1, item:item+1] = text
        logger.info('Only alpahbets success')
        return data

    def stemming(self, data, columns):
        ps = PorterStemmer()
        for item in columns:
            for i in range (len(data)):
                text = str(data[i:i+1, item:item+1])
                text = text[3:-3] #To remove the [['']] from the string
                text = text.split()
                text = [ps.stem(word) for word in text]
                text = ' '.join(text)
                data[i:i+1, item:item+1] = text
        logger.info('Stemming success')
        return data

    def lemmetization(self, data, columns):
        lemmatizer = WordNetLemmatizer()
        for item in columns:
            for i in range (len(data)):
                text = str(data[i:i+1, item:item+1])
                text = text[3:-3]
                text = text.split()
                text = [lemmatizer.lemmatize(word) for word in text]
                text = ' '.join(i for i in text)
                data[i:i+1, item:item+1] = text
        logger.info('Lemmetization success')
        return data
        
    def stopword_removal(self, data, columns):
        for item in columns:
            for i in range (len(data)):
                text = str(data[i:i+1,item:item+1])
                text = text[3:-3]
                text = text.split()
                text = [word for word in text if not word in set(stopwords.words('english'))]
                text = ' '.join(text)
                data[i:i+1, item:item+1] = text
        logger.info('Stopwords removal success')
        return data







