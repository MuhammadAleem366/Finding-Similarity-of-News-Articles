import nltk
from string import punctuation
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import RegexpTokenizer

def Pre_Process(string):
    tokenizer = RegexpTokenizer("[\w']+")
    string = tokenizer.tokenize(string)
    string = [w for w in string if w not in punctuation]
    sw = stopwords.words('english')
    string = [s for s in string if s not in sw ]
    return string