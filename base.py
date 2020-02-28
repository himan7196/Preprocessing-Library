'''Add the name of the package you want to use in the setup.py file'''
import setup
import numpy
import nltk

from nltk.tokenize.toktok import ToktokTokenizer
# Download the required data
# nltk.download('stopwords')
# nltk.download('wordnet')

class Configuration:
    def text_data_configuration(self, only_alpha=False, stem=False, lemma=False, stopword_removal=False, handle_null=False):
        self._only_alpha = only_alpha
        #only porter stemming as of now
        self._stem = stem
        self._lemma = lemma
        self._stopword_removal = stopword_removal
        #null is being handled by removing the value as of now
        self._handle_text_null = handle_null

    def numerical_data_configuration(self, feature_scaling=False, handle_null=False):
        self._feature_scaling = feature_scaling
        self._handle_numeric_null = handle_null


class Numeric():
    def __init__(self, dataframe, *columns):
        if Configuration._handle_numeric_null == True:
            for item in columns:
                self.handle_null(dataframe, item)
        if Configuration._feature_scaling == True:
            for item in columns:
                self.feature_scaling(dataframe, item)


    def feature_scaling(self, dataframe, *columns):
        from sklearn.preprocessing import StandardScaler
        sc = StandardScaler()
        for item in columns:
            dataframe[:, item:item+1] = sc.fit_transform(dataframe[:, item:item+1])
        return dataframe
        

    
    #Currently replacing the NaN by mean
    def handle_null(self, dataframe, *columns):
        from sklearn.impute import SimpleImputer
        imputer = SimpleImputer(missing_values = numpy.nan, strategy = 'mean')
        for item in columns:
            item = int(item)
            imputer = imputer.fit(dataframe[:,item:item+1])
            dataframe[:,item:item+1] = imputer.transform(dataframe[:,item:item+1])
        return dataframe
        


class Text ():
    def __init__(self, dataframe, *columns):
        if Configuration._only_alpha==True:
            for item in columns:
                self.only_alphabets(dataframe, item)
        if Configuration._stem==True:
            for item in columns:
                self.stemming(dataframe, item)
        if Configuration._lemma==True:
            for item in columns:
                self.lemmetization(dataframe, item)
        if Configuration._stopword_removal==True:
            for item in columns:
                self.stopword_removal(dataframe, item)
        if Configuration._handle_text_null==True:
            for item in columns:
                self.handle_null(dataframe, item)
        

    def only_alphabets(self, dataframe, *columns):
        '''How to handle nltk.download('stopwords')'''
        import re
        from nltk.stem.porter import PorterStemmer
        from nltk.corpus import stopwords
        for item in columns:
            for i in range (len(dataframe)):
                text = re.sub('[^a-zA-Z]', ' ', str(dataframe[i:i+1,item:item+1]))
                text = re.sub(' +', ' ', text)
                text = text.lower()
                #text = text.split()
                #ps = PorterStemmer()
                #text = [ps.stem(word) for word in text if not word in set(stopwords.words('english'))]
                #text = ' '.join(text)
                dataframe[i:i+1, item:item+1] = text

        return dataframe

    def stemming(self, dataframe, *columns):
        '''Does porter stemming only as of now'''
        from nltk.stem.porter import PorterStemmer
        ps = PorterStemmer()
        for item in columns:
            for i in range (len(dataframe)):
                text = str(dataframe[i:i+1, item:item+1])
                text = text[3:-3] #To remove the [['']] from the string
                text = text.split()
                text = [ps.stem(word) for word in text]
                text = ' '.join(text)
                dataframe[i:i+1, item:item+1] = text

        return dataframe

    def lemmetization(self, dataframe, *columns):
        from nltk.stem import WordNetLemmatizer
        lemmatizer = WordNetLemmatizer()
        for item in columns:
            for i in range (len(dataframe)):
                text = str(dataframe[i:i+1, item:item+1])
                text = text[3:-3]
                text = text.split()
                text = [lemmatizer.lemmatize(word) for word in text]
                text = ' '.join(i for i in text)
                dataframe[i:i+1, item:item+1] = text
        return dataframe
        
    def stopword_removal(self, dataframe, *columns):
        from nltk.corpus import stopwords
        for item in columns:
            for i in range (len(dataframe)):
                text = str(dataframe[i:i+1,item:item+1])
                text = text[3:-3]
                text = text.split()
                text = [word for word in text if not word in set(stopwords.words('english'))]
                text = ' '.join(text)
                dataframe[i:i+1, item:item+1] = text

        return dataframe

    def handle_null(self):
        pass






