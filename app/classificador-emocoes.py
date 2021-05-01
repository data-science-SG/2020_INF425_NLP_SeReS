import streamlit as st
import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
import torch
import tweepy as tw
import seaborn as sns

import time

from gensim.models import KeyedVectors
from gensim.test.utils import datapath, get_tmpfile
from gensim.scripts.glove2word2vec import glove2word2vec
import os
from googletrans import Translator
tradutor = Translator(service_urls=['translate.googleapis.com'])

from nltk.tokenize import TweetTokenizer
import sys
sys.path.append('.\app')

import modelClass
from modelClass import *

## ------------------- Variáveis globais --------------------------------

tknzr = TweetTokenizer()
cwd = os.getcwd()

# Tratanto secrets
#secret_access_token = st.secrets['secret_access_token']
#secret_access_token_secret = st.secrets['secret_access_token_secret']
#secret_api_key = st.secrets['secret_api_key']
#secret_api_key_secret = st.secrets['secret_api_key_secret']

## ------------------- Pré configurações -------------------------------

pd.set_option('display.max_colwidth', -1)
pd.set_option('display.max_rows', None)

## ------------------- API do twitter ----------------------------------

access_token = '830182504468533248-uysXPZQhVDUrPXwjlyuAbV9YAGNWjwQ'
access_token_secret = 'bX2QVMH7HWgWs3uxnVL5dbQx8eqONF5TQ6kzkrm2LUG44'

API_key = 'Gjihyy0lww3s4eSsHS0LtbZ3X' # consumer_key 
API_secret_key = '5FE2zFVCkMLYZuK0G6nvvQ4YZgZW8YbN14z4VMXrUyRujMjYyl'

auth = tw.OAuthHandler(API_key, API_secret_key )             # método OAuthHandler da biblioteca tw: 
                                                             # -- cria o objeto authentication handler: usa "consumer_key" e "consumer_secret"
auth.set_access_token(access_token, access_token_secret )    # método "set_access_token" do objeto auth: usa "key" e "secret" (dos 'tokens') 
api = tw.API(auth, wait_on_rate_limit=True)                  # método API da biblioteca tw: recebe acesso para o uso da API com oobjeto api

## ------------------- Funções ----------------------------------------

def createSpaces():
    '''
    Cria um espaço para separar as informaçç
    '''
    st.write('#')

def showProgressBar(sleep=0.01):
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(sleep)
        my_bar.progress(percent_complete + 1)

def cleanText(x):
    '''
    Recebe uma frase e remove as "\n", retornando a mesma
    '''
    return x.replace('\n', ' ')

def translate(doc, src='pt', dest='en'):
    '''
    Recebe uma palavra e a traduz para o idioma de destino
    '''
    result = tradutor.translate(doc, src=src, dest=dest).text
    return result

def label2Embedding(word):
  ''' Recebe uma string (word) e devolve o embedding vector correspondente (se existir).
  '''
  if word in modelo.vocab:
    embed = modelo.get_vector(word)
    if embed is not None:
      return embed

def convertTokens(tweets, max_len=150, num_dims=100):
    '''
    Recebe uma lista de tweets e converte os tokens pelo seu embedding, concatenando  o valor 0 para completar o tamanho máximo de palavras definida
    '''
    # Convertendo os tokens pelo seu embedding com um tamanho máximo de 150
    max_len = max_len       # comprimento máximo da mensagem (em número de palavras)
    encoded_docs = []    # inicializa a lista de documentos codificados

    for sentence in tweets: # para cada token
        encoded_d = [label2Embedding(t) for t in sentence]
        encoded_d = [vec.tolist() for vec in encoded_d if vec is not None]
        # adiciona o padding, se necessário
        padding_word_vecs = [np.zeros(num_dims).tolist()]*max(0, max_len-len(encoded_d)) 
        encoded_d = padding_word_vecs + encoded_d
        # trunca o documento e salva na lista de documentos codificados
        encoded_docs.append(encoded_d[:max_len]) 

    encoded_docs_arrays = [np.vstack(sentence) for sentence in encoded_docs]
    return encoded_docs_arrays


@st.cache
def load_word_embedding(num_dims=100):
    glove_file = datapath(cwd+f'/eda/data/glove.6B.{num_dims}d.txt')
    tmp_file   = get_tmpfile(cwd+f"/eda/data/glove.6B.{num_dims}d_word2vec.txt")
    _          = glove2word2vec(glove_file, tmp_file)

    filename_txt = cwd+f"/eda/data/glove.6B.{num_dims}d_word2vec.txt"
    return KeyedVectors.load_word2vec_format(filename_txt)


## ------------------- Começo da página -----------------------------------

modelo = load_word_embedding()

st.title('Modelo Classificador de Emoções')

st.header('Sobre o projeto')

st.write('''O projeto referenciado no presente relatório se consiste na tarefa de construir um algoritmo, utilizando dos conceitos de Machine Learning e 
Data Science, que seja capaz de identificar, através de análises textuais de tweets retiradas da rede social Twitter, a emoção imposta no texto, em foco 
para possíveis sinais de depressão. Vale ressaltar a diferença entre análise de emoções e análise de sentimentos. Ao nos referirmos a análise de emoções, 
estamos focando em algo mais específico, como alegria, tristeza, raiva, surpresa, entre outros. Diferente da análise de sentimentos, que diz respeito ao 
sentimento expresso pelo texto, normalmente sendo classificados como positivo, negativo e neutro. ''')

st.subheader('Sobre a uso da ferramenta')

st.write('''Para utilizar a página, você deve inserir seu nome de usuário no campo abaixo. Após isso, clique no botão *Executar algoritmo* logo abaixo. 
Após isso, o sistema irá buscar seus tweets em sua conta e irá executar o Algoritmo Classificador de Emoções, mostrando logo abaixo o resultado obtido''')

createSpaces()

username = st.text_input('Insira o usuário:')

if (st.button('Executar algoritmo')):
    createSpaces()

    qtd_tweets = 3
    filters = " -filter:mentions -filter:retweets -filter:images -filter:native_video -filter:links" #Filtro
    user = 'from:' + username.replace("@", "")

    st.markdown('*Coletando seus tweets...*')
    showProgressBar()

    search_string = user + filters     
    tweets = tw.Cursor(api.search, q=search_string, tweet_mode='extended', lang="pt",).items(qtd_tweets)
    users_locs = [[tweet.user.screen_name, tweet.full_text] for tweet in tweets]

    tweets_dataframe = pd.DataFrame()
    tweets_dataframe = pd.DataFrame(data=users_locs, columns=['usuario', "texto"])

    if len(tweets_dataframe) >= 3:
        tweets_dataframe['texto_limpo'] = tweets_dataframe['texto'].apply(cleanText)
        
        st.write('Aqui estão os seus tweets que coletamos para fazer a análise')
        st.write(tweets_dataframe[['usuario','texto_limpo']].to_markdown())

        ## Traduzir o texto para inglês
        tweets_dataframe['texto_traduzido'] = tweets_dataframe['texto_limpo'].apply(lambda x: translate(x))
        
        createSpaces()
        st.markdown('*Traduzindo seus tweets...*')
        showProgressBar(0.001)

        st.write('Aqui estão os seus tweets traduzidos')
        st.write(tweets_dataframe[['usuario','texto_limpo', 'texto_traduzido']].to_markdown())

        createSpaces()    
        # Transformando as frases em tokens
        tweets_dataframe["texto_traduzido"] = [tknzr.tokenize(sentence) for sentence in tweets_dataframe["texto_traduzido"]]

        encoded_docs_arrays = convertTokens(tweets_dataframe["texto_traduzido"])

        tweets_dataframe['X'] = pd.Series(encoded_docs_arrays)
        X = np.dstack(tweets_dataframe['X'].values).transpose(2,0,1)
        X = torch.FloatTensor(X)

        # Carregando o modelo
        st.markdown('*Carregando o modelo classificador de emoções...*')
        showProgressBar()
        model = torch.load(cwd+"/models/emotions_classifier_LSTM.pth", map_location=torch.device('cpu'))
        model.eval()

        createSpaces()    
        st.markdown('*Calculando suas emoções...*')
        showProgressBar()
        # Fazendo predições
        preds = model.forward(X)

        ## Mostrando o quadro da distribuição de emoções
        emotions = ['Raiva','Desgosto','Medo','Felicidade','Tristeza','Surpresa']
        preds = preds.detach().numpy()
        preds_probs = np.exp(preds)

        st.write('Aqui está os gráficos das distribuições das emoções que o nosso modelo classificou')
        fig, ax = plt.subplots(nrows=qtd_tweets,ncols=1,figsize=(10, 6))

        for i, array in enumerate(preds_probs):   
            ax[i].set_title(tweets_dataframe['texto_limpo'][i])
            ax[i].bar(x=emotions, height=array, color=['lightcoral', 'khaki', 'bisque', 'lightsteelblue', 'lightgreen', 'thistle'])
        
        fig.tight_layout(pad=3.0)
        st.pyplot(fig)

    
    else:
        st.write('Desculpe, não conseguimos utilizar os tweets deste usuário para fazer a análise :(')
        st.write('''Certifique-se de que o usuário possui, no mínimo, 3 tweets públicos, que ele não esteja 
                 com a conta no modo privado e que o mesmo possui tweets que não sejam: menções, retweets, 
                 que não contenha imagens ou vídeos e que não contenha links de forma geral.''')
        
        createSpaces()

        st.markdown('''**Importante:** Mesmo que o usuário altere a conta do modo privado, ele deverá
                    ter realizado algum tweet com a conta já publica para que o mesmo possa ser
                    coletado!''')


    
  

