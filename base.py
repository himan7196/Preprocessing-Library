'''Add the name of the package you want to use in the file'''
import numpy
import nltk
import re
import sklearn
import numpy
import nltk
import regex
    
from nltk.tokenize.toktok import ToktokTokenizer
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
# Download the required data
# nltk.download('stopwords')
# nltk.download('wordnet')

class Categorical:
    pass



class Numeric():
    def __init__(self, feature_scaling, handle_null, data, columns):
        if handle_null == True:
            self.handle_null(data, columns)
        if feature_scaling == True:
            self.feature_scaling(data, columns)


    def feature_scaling(self, data, columns):
        sc = StandardScaler()
        for item in columns:
            data[:, item:item+1] = sc.fit_transform(data[:, item:item+1])
        return data
        

    
    #Currently replacing the NaN by mean
    def handle_null(self, data, columns):
        imputer = SimpleImputer(missing_values = numpy.nan, strategy = 'mean')
        for item in columns:
            item = int(item)
            imputer = imputer.fit(data[:,item:item+1])
            data[:,item:item+1] = imputer.transform(data[:,item:item+1])
        return data
        


class Text ():
    def __init__(self, only_alpha, stem, lemma, stopword_removal, handle_null, data, columns):
        if only_alpha==True:
            self.only_alphabets(data, columns)
        if stem==True:
            self.stemming(data, columns)
        if lemma==True:
            self.lemmetization(data, columns)
        if stopword_removal==True:
            self.stopword_removal(data, columns)
        if handle_null==True:
            self.handle_null(data, columns)
        

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

        return data

    def handle_null(self):
        pass






