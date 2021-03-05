#Imports
import re
import nltk
from nltk.stem import PorterStemmer
import nltk
nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('english')
ps = PorterStemmer()


def cria_dicio(txt,logic, dicio={}):
  """
  Função que cria um dicionário da seguinte maneira: (palavra, classe) : contagem

  **Parametros:**
  txt: array-like 
    Texto que irá ser armazenado no dicionário

  logic: binary
    Classe da frase, sendo 1-positiva e 0-negativa 

  dicio: dict, default empty
    Dicionário onde irá armazenar as palavras

  **Output*
    Retorna um dicionário (palavra, classe) : contagem
  """
  for text, classe in zip(txt,logic):
      for word in text:
        if word != '':
          #Cria a chave
          key = (word, classe) 
          #Adciona a palavra ao dicionário e se ela já se encontra, acrescenta +1 na contagem
          if key in dicio:
            dicio[key] += 1 
          else:
            dicio[key] = 1

  return dicio

def cria_vetor(df,txt, dicio, pos=0, neg=0):
  """
  Função que cria um vetor da seguinte maneira: [1, Soma das frequências (palavra, classe=1), Soma das frequências (palavra, classe=0)]

  **Parametros**
  txt: array-like 
    Texto que irá ser armazenado no dicionário

  dicio: dict
    Dicionário onde contém as palavras com a contagem

  pos: int, default empty
    Variável que contabiliza a soma das frequências das palavras positivas(1)

  neg: int, default empty
    Variável que contabiliza a soma das frequências das palavras negativas(0)

  **Output**
    Retorna um vetor de três dimensões: [1, Soma das frequências (palavra, classe=1), Soma das frequências (palavra, classe=0)]
  """

  words = set(txt)
  for word in words:
    pos += dicio.get((word, 1), 0)
    neg += dicio.get((word, 0), 0)
    
    df['Vetor Constante'] = 1
    df['Vetor Positivo'] = pos
    df['Vetor Negativo'] = neg

  return df

