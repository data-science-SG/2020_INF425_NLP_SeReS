import string
import re
import nltk
from nltk.tokenize import TweetTokenizer
import re
from nltk import FreqDist
from nltk.tokenize import TweetTokenizer
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords 

nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words("english")
token_espaço = nltk.tokenize.WhitespaceTokenizer()

def clean_text(words, stem=False):
  """ Remove stopwords, punctuation, special caracters, etc from the received text.

  Keywords arguments:
  words -- text to be cleaned
  stem -- stem words or dont (default false)
    
  """
  newWords = list()
  pontuacao = string,
  for word in words:
    word = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'\
                       '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', word)
    words = re.sub("(@[A-Za-z0-9_]+)","", word)
    if len(word) > 0 and words not in string.punctuation and word.lower() not in stopwords and word.lower != "<br />":
      if stem:
        word = stemmer.stem(word.lower())
        newWords.append(word)
      else:
        newWords.append(word.lower())

  return newWords