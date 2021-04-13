import streamlit as st
import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
import torch
import tweepy as tw

import time

from gensim.models import KeyedVectors
from gensim.test.utils import datapath, get_tmpfile
from gensim.scripts.glove2word2vec import glove2word2vec
import os
from googletrans import Translator
tradutor = Translator(service_urls=['translate.googleapis.com'])


## ------------------- Funções --------------------------------

def cleanText(x):
    return x.replace('\n', ' ')

def translate(doc):
    print(doc)
    result = tradutor.translate(doc, src='pt', dest='en').text
    return result

def label2Embedding(sentence):
  for word in sentence: 
    if word in modelo.vocab:
      embed = modelo.get_vector(word)
      if embed is not None:
        return embed

def convertTokens(tweets):
    max_len = 53         # comprimento máximo da mensagem (em número de palavras)
    encoded_docs = []    # inicializa a lista de documentos codificados

    for token in tweets: # para cada token
        encoded_d = [label2Embedding(t) for t in token]
        encoded_d = [vec.tolist() for vec in encoded_d if vec is not None]

        # adiciona o padding, se necessário
        padding_word_vecs = [np.zeros(50).tolist()]*max(0, max_len-len(encoded_d)) 
        encoded_d = padding_word_vecs + encoded_d
  
        # trunca o documento e salva na lista de documentos codificados
        encoded_docs.append(encoded_d[:max_len]) 


    encoded_docs_arrays = [np.vstack(sentence) for sentence in encoded_docs]
    return encoded_docs_arrays    

## ------------------------------------------------------------

## Carregando os Word Embedding
cwd = os.getcwd()

glove_file = datapath(cwd+'/eda/data/glove.6B.50d.txt')
tmp_file   = get_tmpfile(cwd+"/eda/data/glove.6B.50d_word2vec.txt")
_          = glove2word2vec(glove_file, tmp_file)

filename_txt = cwd+"/eda/data/glove.6B.50d_word2vec.txt"
modelo = KeyedVectors.load_word2vec_format(filename_txt)


##  ------------------ Configurações Twitter API -------------------------------

#Visualização de dados
pd.set_option('display.max_colwidth', -1)
pd.set_option('display.max_rows', None)

#API do twitter


## Secret Keys
access_token = '830182504468533248-uysXPZQhVDUrPXwjlyuAbV9YAGNWjwQ'
access_token_secret = 'bX2QVMH7HWgWs3uxnVL5dbQx8eqONF5TQ6kzkrm2LUG44'

API_key = 'Gjihyy0lww3s4eSsHS0LtbZ3X' # consumer_key 
API_secret_key = '5FE2zFVCkMLYZuK0G6nvvQ4YZgZW8YbN14z4VMXrUyRujMjYyl'

auth = tw.OAuthHandler(API_key, API_secret_key )             # método OAuthHandler da biblioteca tw: 
                                                             # -- cria o objeto authentication handler: usa "consumer_key" e "consumer_secret"
auth.set_access_token(access_token, access_token_secret )    # método "set_access_token" do objeto auth: usa "key" e "secret" (dos 'tokens') 
api = tw.API(auth, wait_on_rate_limit=True)                  # método API da biblioteca tw: recebe acesso para o uso da API com oobjeto api

## ----------------------------------------------------------------------------

## Title
st.title('Modelo Classificador de Emoções')
st.subheader('(com usuário dinâmico)')

## Explicação básica do projeto
st.header('Sobre o projeto')

about = 'O projeto referenciado no presente relatório se consiste na tarefa de construir um algoritmo, utilizando dos conceitos de Machine Learning e Data Science, que seja capaz de identificar, através de análises textuais de tweets retiradas da rede social Twitter, a emoção imposta no texto, em foco para possíveis sinais de depressão. Vale ressaltar a diferença entre análise de emoções e análise de sentimentos. Ao nos referirmos a análise de emoções, estamos focando em algo mais específico, como alegria, tristeza, raiva, surpresa, entre outros. Diferente da análise de sentimentos, que diz respeito ao sentimento expresso pelo texto, normalmente sendo classificados como positivo, negativo e neutro. '
st.write(about)

## Explicação sobre a página
st.subheader('Sobre a uso da ferramenta')
algorithm = 'Para utilizar a página, você deve inserir seu nome de usuário no campo abaixo. Após isso, clique no botão *Executar algoritmo* logo abaixo. Após isso, o sistema irá buscar seus tweets em sua conta e irá executar o Algoritmo Classificador de Emoções, mostrando logo abaixo o resultado obtido'
st.write(algorithm)

##  Input do usuário
# Alguns espaços
for x in [''] * 4:
    st.text(x)

username = st.text_input('Insira o usuário:')

## Botão de rodar algoritmo

tweets_dataframe = pd.DataFrame()

if (st.button('Executar algoritmo')):
    qtd_tweets = 10
    # my_bar = st.progress(0)
    # for percent_complete in range(tweets_dataframe.size):
    #     time.sleep(0.1)
    #     my_bar.progress(percent_complete + 1)

    #Exibir os tweets e realizar a pesquisa
    filters = " -filter:mentions -filter:retweets -filter:images -filter:native_video -filter:links" #Filtro
    user = 'from:' + username.replace("@", "")

    search_string = user + filters     
    tweets = tw.Cursor(api.search, q=search_string, tweet_mode='extended', lang="pt",).items(qtd_tweets)
    users_locs = [[tweet.user.screen_name, tweet.full_text] for tweet in tweets]
    tweets_dataframe = pd.DataFrame(data=users_locs, columns=['usuario', "texto"])

    # Limpar os \n por '' (.apply(function clean_text())) e mostrando com .to_markdown()
    tweets_dataframe['texto_limpo'] = tweets_dataframe['texto'].apply(cleanText)
    st.write(tweets_dataframe[['usuario','texto_limpo']].to_markdown())

    # tweets_dataframe.to_csv("teste.txt", header=None, index=None, sep='\t')
    # st.dataframe(data=tweets_dataframe, width=1600)
    # st.text([tweet for _, tweet in users_locs])

    for x in [''] * 4:
        st.text(x)

    ## Traduzir o texto para inglês -----------------------------------------------------------
    tweets_dataframe['texto_traduzido'] = tweets_dataframe['texto_limpo'].apply(lambda x: translate(x))
    st.write(tweets_dataframe[['usuario','texto_limpo', 'texto_traduzido']].to_markdown())

            # Carregando o modelo
    model = torch.load(cwd+"/models/emotions_classifier.pth")

    st.write('----------------  MODEL', model.eval())

        # Carregando o dicionario
    loaded_dict = model.load_state_dict(torch.load(cwd+"/dicts/emotions_classifier_dict"))

    st.write('LOADED DICT -------------------', loaded_dict)

    e = next(model.embeddings[0].parameters())
    st.write('------------- E,DATA',e.data)

    tweets_dataframe['X'] = convertTokens(tweets_dataframe['texto_traduzido'])
    X_test = np.vstack(tweets_dataframe['X'])
    X_test = torch.LongTensor(X_test)

    preds = model.forward(X_test)

    st.write("------------------ DATAFRAME X",tweets_dataframe['X'])
    st.write("---------  PREDS",preds)

    tweets_dataframe["previsoes"] = [torch.exp(pred).detach().numpy() for pred in preds]

    ## Passar para o modelo classificador de emoções -------------------------------------------
    


    ## Mostrando o quadro da distribuição de emoções
    feelings = {'Angry': 0,'Disgust': 1,'Fear': 2,'Happy': 3,'Sad': 4,'Surprise': 5}
    emotions = list(moods.keys())

    #usuario = X_test_df.set_index('user').loc[usuario_teste][0]
    #usuario = usuario.reshape(-1)
    #sns.barplot(y=usuario,x=emotions)


    #X_test = np.vstack(tweets_dataframe['doc_processado'])
    #X_test = torch.LongTensor(X_test)

    #prediction = model.predict([tweets_dataframe['texto_traduzido']])

