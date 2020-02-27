'''Add the name of the package you want to use in the setup.py file'''
#import setup
import numpy
import nltk

from nltk.tokenize.toktok import ToktokTokenizer
# Download the required data
# nltk.download('stopwords')

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
        #will replace the null value by the mean of all values as of now
        self._handle_numeric_null = handle_null


class Numeric():
    def __init__(self):
        if Configuration._handle_numeric_null == True:
            self.handle_null()
        if Configuration._feature_scaling == True:
            self.feature_scaling()


    def feature_scaling(self, dataframe, *columns):
        from sklearn.preprocessing import StandardScaler
        sc = StandardScaler()
        for item in columns:
            dataframe[:, item:item+1] = sc.fit_transform(dataframe[:, item:item+1])
        print('Feature scaling completed')
        return dataframe

    
    #Currently replacing the NaN by mean
    def handle_null(self, dataframe, *columns):
        from sklearn.impute import SimpleImputer
        imputer = SimpleImputer(missing_values = numpy.nan, strategy = 'mean')
        for item in columns:
            item = int(item)
            imputer = imputer.fit(dataframe[:,item:item+1])
            dataframe[:,item:item+1] = imputer.transform(dataframe[:,item:item+1])
        print('Null handling completed')
        return dataframe
        
        #print('I do the handling null for numbers')


class Text ():
    def __init__(self, text):

        if Configuration._only_alpha==True:
            self.only_alphabets()
        if Configuration._stem==True:
            self.stemming()
        if Configuration._lemma==True:
            self.lemmetization()
        if Configuration._stopword_removal==True:
            self.stopword_removal()
        if Configuration._handle_text_null==True:
            self.handle_null()

    def only_alphabets(self):
        pass

    def stemming(self, text):
        ps = nltk.PorterStemmer()
        text = ' '.join([ps.stem(word) for word in text.split()])
        return text

    def lemmetization(self, text):
        lemmatizer = WordNetLemmatizer()
        token_list = [i for i in text.split(' ')]
        lemma_list = [lemmatizer.lemmatize(i) for i in token_list]
        new_text = ' '.join(i for i in lemma_list)
        return new_text

    def stopword_removal(self, text, is_lower_case=False):
        stopword_list = nltk.corpus.stopwords.words('english')
        tokenizer = ToktokTokenizer()
        tokens = tokenizer.tokenize(text)
        tokens = [token.strip() for token in tokens]
        if is_lower_case:
            filtered_tokens = [token for token in tokens if token not in stopword_list]
        else:
            filtered_tokens = [token for token in tokens if token.lower() not in stopword_list]
        filtered_text = ' '.join(filtered_tokens)
        return filtered_text

    def handle_null(self):
        pass






