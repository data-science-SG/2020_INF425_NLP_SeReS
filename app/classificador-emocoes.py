import streamlit as st
import numpy as np
import pandas as pd

import time

##  ------------------ Configurações Twitter API -------------------------------

#Visualização de dados
import pandas as pd
pd.set_option('display.max_colwidth', -1)
pd.set_option('display.max_rows', None)

#API do twitter
import tweepy as tw


## Secret Keys
access_token = '830182504468533248-uysXPZQhVDUrPXwjlyuAbV9YAGNWjwQ'
access_token_secret = 'bX2QVMH7HWgWs3uxnVL5dbQx8eqONF5TQ6kzkrm2LUG44'

API_key = 'Gjihyy0lww3s4eSsHS0LtbZ3X' # consumer_key 
API_secret_key = '5FE2zFVCkMLYZuK0G6nvvQ4YZgZW8YbN14z4VMXrUyRujMjYyl'

auth = tw.OAuthHandler(API_key, API_secret_key )             # método OAuthHandler da biblioteca tw: 
                                                             # -- cria o objeto authentication handler: usa "consumer_key" e "consumer_secret"
auth.set_access_token(access_token, access_token_secret )    # método "set_access_token" do objeto auth: usa "key" e "secret" (dos 'tokens') 
api = tw.API(auth, wait_on_rate_limit=True)                  # método API da biblioteca tw: recebe acesso para o uso da API com oobjeto api

print(type(auth),type(api))

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
empty = ['','','','']
for x in empty:
    st.text(x)

username = st.text_input('Insira o usuário:')

## Botão de rodar algoritmo

tweets_dataframe = []

if (st.button('Executar algoritmo')):
    #Escolhendo a quantidade de tweets q vou pegar :)
    num_itens_depre = 600
    num_itens_sad = 10

    #Quantos tweets do usuário coletar
    num_tweets_depre = 10
    num_tweets_sad = 4

    #Mínimo de tweets que o usuário deve ter para entrar no dataset
    min_tweets = 3

    #Exibir os tweets e realizar a pesquisa

    filters = "-filter:mentions -filter:retweets -filter:images -filter:native_video -filter:links" #Filtro
    user = 'from:' + username.replace("@", "")

    search_string = user

    search_string
                                                                       
    tweets = tw.Cursor(api.search, q=search_string, tweet_mode='extended', lang="pt",).items(10)

    tweets

    users_locs = [[tweet.user.screen_name, tweet.full_text] for tweet in tweets]

    users_locs

    tweets_dataframe =  pd.DataFrame(data=users_locs, columns=['usuario', "texto"])

    tweets_dataframe.head()


    # Alguns espaços
    # empty = ['','']
    # for x in empty:
    #     st.text(x)
    # my_bar = st.progress(0)
    # for percent_complete in range(500):
    #     time.sleep(0.1)
    #     my_bar.progress(percent_complete + 1)