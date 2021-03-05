#Imports
import re
import nltk
from nltk.stem import PorterStemmer
import nltk
nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('english')
ps = PorterStemmer()

#Função
def clean_text(txt, STEM = True):
  """
  Função que limpa um texto
  STEAM = Ativa o Stemmer

  **Parametros**
   txt: array-like 
    Texto que irá ser armazenado no dicionário
  
  STEAM: boolean, default true
    Se True, utiliza a função stem

  **Output**
  Retorna o Txt com o texto limpo

  """
  #Tirar maiúsculas
  transformTxt = txt.lower()
  #Tirar esse demônio de espaço <br />
  transformTxt = transformTxt.replace("<br />","")
  #Remover pontuação
  transformTxt = transformTxt.replace("[^\w\s]","")
  #Tokenizar
  transformTxt = re.split("\W+", transformTxt)
  #Se livrar das Stopwords
  transformTxt = [word for word in transformTxt if word not in stopwords]
  #Deixar no infinitivo
  if STEM == True:
    transformTxt = [ps.stem(word) for word in transformTxt]

  return transformTxt