'''Add the name of the package you want to use in the setup.py file'''
import setup
import numpy
import nltk

from nltk.tokenize.toktok import ToktokTokenizer
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
# Download the required data
# nltk.download('stopwords')
# nltk.download('wordnet')

class Categorical:
    pass



class Numeric():
    def __init__(self, feature_scaling, handle_null, dataframe, columns):
        if handle_null == True:
            self.handle_null(dataframe, columns)
        if feature_scaling == True:
            self.feature_scaling(dataframe, columns)


    def feature_scaling(self, dataframe, columns):
        sc = StandardScaler()
        for item in columns:
            dataframe[:, item:item+1] = sc.fit_transform(dataframe[:, item:item+1])
        return dataframe
        

    
    #Currently replacing the NaN by mean
    def handle_null(self, dataframe, columns):
        imputer = SimpleImputer(missing_values = numpy.nan, strategy = 'mean')
        for item in columns:
            item = int(item)
            imputer = imputer.fit(dataframe[:,item:item+1])
            dataframe[:,item:item+1] = imputer.transform(dataframe[:,item:item+1])
        return dataframe
        


class Text ():
    def __init__(self, only_alpha, stem, lemma, stopword_removal, handle_null, dataframe, columns):
        if only_alpha==True:
            self.only_alphabets(dataframe, columns)
        if stem==True:
            self.stemming(dataframe, columns)
        if lemma==True:
            self.lemmetization(dataframe, columns)
        if stopword_removal==True:
            self.stopword_removal(dataframe, columns)
        if handle_null==True:
            self.handle_null(dataframe, columns)
        

    def only_alphabets(self, dataframe, columns):
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

    def stemming(self, dataframe, columns):
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

    def lemmetization(self, dataframe, columns):
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
        
    def stopword_removal(self, dataframe, columns):
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






