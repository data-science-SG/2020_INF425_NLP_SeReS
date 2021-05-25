import numpy as np

from googletrans import Translator
tradutor = Translator(service_urls=['translate.googleapis.com'])
import string
import re
import nltk
from nltk.corpus import stopwords 
from nltk.stem import PorterStemmer
from nltk.tokenize import TweetTokenizer

tknzr = TweetTokenizer()
stemmer = PorterStemmer()
nltk.download('punkt')

nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words("english")

def cleanText(sentence, stem=False):
    """ Remove stopwords, punctuation, special caracters, etc from the received text.
    Keywords arguments:
    words -- text to be cleaned
    stem -- stem words or dont (default false)
    """

    return sentence.replace('\n', ' ')
    
    # newWords = list()
    # pontuacao = string,
    # sentence.replace('\n', ' ')
    # for word in sentence:
    #     word = word.lower()
    #     word = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'\
    #                    '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', word)
    # words = re.sub("(@[A-Za-z0-9_]+)","", word)
    # if len(word) > 0 and word not in string.punctuation and word not in stopwords and word != "<br />":
    #   if stem:
    #     word = stemmer.stem(word.lower())
    #     newWords.append(word)
    #   else:
    #     newWords.append(word.lower())

    # return newWords

def translate(doc, src='pt', dest='en'):
    '''
    Recebe uma palavra e a traduz para o idioma de destino
    '''
    result = tradutor.translate(doc, src=src, dest=dest).text
    return result

def label2Embedding(word, modelo):
  ''' Recebe uma string (word) e devolve o embedding vector correspondente (se existir).
  '''
  if word in modelo.vocab:
    embed = modelo.get_vector(word)
    if embed is not None:
      return embed

def convertTokens(tweets, modelo, max_len=150, num_dims=100):
    '''
    Recebe uma lista de tweets e converte os tokens pelo seu embedding, concatenando  o valor 0 para completar o tamanho máximo de palavras definida
    '''
    # Convertendo os tokens pelo seu embedding com um tamanho máximo de 150
    max_len = max_len       # comprimento máximo da mensagem (em número de palavras)
    encoded_docs = []    # inicializa a lista de documentos codificados

    for sentence in tweets: # para cada token
        encoded_d = [label2Embedding(t, modelo) for t in sentence]
        encoded_d = [vec.tolist() for vec in encoded_d if vec is not None]
        # adiciona o padding, se necessário
        padding_word_vecs = [np.zeros(num_dims).tolist()]*max(0, max_len-len(encoded_d)) 
        encoded_d = padding_word_vecs + encoded_d
        # trunca o documento e salva na lista de documentos codificados
        encoded_docs.append(encoded_d[:max_len]) 

    encoded_docs_arrays = [np.vstack(sentence) for sentence in encoded_docs]
    return encoded_docs_arrays
