import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import torch
import tweepy as tw
import seaborn as sns
from pathlib import Path

from gensim.models import KeyedVectors
from gensim.test.utils import datapath, get_tmpfile
from gensim.scripts.glove2word2vec import glove2word2vec
import os
from googletrans import Translator
tradutor = Translator(service_urls=['translate.googleapis.com'])

from nltk.tokenize import TweetTokenizer
import sys
sys.path.append('.\app')

from modelClass import *
from depressionModelClass import *

from page_layout import createSpaces, showProgressBar
from text_manipulation import cleanText, translate, convertTokens, breakPlotTitle

## ------------------- Variáveis globais --------------------------------

tknzr = TweetTokenizer()
cwd = os.getcwd()
min_depression_tweets = 6

# Tratanto secrets
secret_access_token = st.secrets["SECRET_ACCESS_TOKEN"]
secret_access_token_secret = st.secrets["SECRET_ACCESS_TOKEN_SECRET"]
secret_api_key = st.secrets["SECRET_API_KEY"]
secret_api_key_secret = st.secrets["SECRET_API_KEY_SECRET"]

## ------------------- Pré configurações -------------------------------

pd.set_option('display.max_colwidth', -1)
pd.set_option('display.max_rows', None)

## ------------------- API do twitter ----------------------------------

access_token = secret_access_token
access_token_secret = secret_access_token_secret

API_key = secret_api_key # consumer_key 
API_secret_key = secret_api_key_secret

auth = tw.OAuthHandler(API_key, API_secret_key )             # método OAuthHandler da biblioteca tw: 
                                                             # -- cria o objeto authentication handler: usa "consumer_key" e "consumer_secret"
auth.set_access_token(access_token, access_token_secret )    # método "set_access_token" do objeto auth: usa "key" e "secret" (dos 'tokens') 
api = tw.API(auth, wait_on_rate_limit=True)                  # método API da biblioteca tw: recebe acesso para o uso da API com oobjeto api

## ------------------- Funções ----------------------------------------

# criar função decoradora que declara o modelo

## ------------------- Começo da página -----------------------------------
def main():
    st.title('Modelo Classificador de Emoções')

    st.header('Sobre o projeto')
    st.write('''O projeto referenciado no presente relatório se consiste na tarefa de construir um algoritmo, utilizando dos conceitos de Machine Learning e 
    Data Science, que seja capaz de identificar, através de análises textuais de tweets retiradas da rede social Twitter, a emoção imposta no texto, em foco 
    para possíveis sinais de depressão. Vale ressaltar a diferença entre análise de emoções e análise de sentimentos. Ao nos referirmos a análise de emoções, 
    estamos focando em algo mais específico, como alegria, tristeza, raiva, surpresa, entre outros. Diferente da análise de sentimentos, que diz respeito ao 
    sentimento expresso pelo texto, normalmente sendo classificados como positivo, negativo e neutro. ''')
    
    st.markdown('### Contato')
    st.markdown('**Link do projeto no GitHub: https://github.com/data-science-SG/2020_INF425_NLP_SeReS**')
    st.markdown('##### **E-mail para contato:**')
    st.write('carlosgreinheimer@gmail.com')
    st.write('eduardasorgetzalves@gmail.com')
    st.write('fontanads@gmail.com')

    st.subheader('Sobre a uso da ferramenta')
    st.write('''Para utilizar a página, você deve inserir algum nome de usuário no campo abaixo. Após isso, clique no botão *Executar algoritmo* logo abaixo. 
    Dessa forma o sistema irá buscar os tweets da conta e irá executar o Algoritmo Classificador de Emoções e o Algaritmo Classificador de Depressão, mostrando o resultado obtido''')
    st.write('''Fique atento que a busca é realizada buscando tweets em português, portanto tweets em qualquer outro idioma não serão coletados''')

    st.subheader('Sobre os resultados')
    st.markdown('''Primeiramente, vale ressaltar que diversos fatores afetaram o resultado do algoritmo.''')
    st.markdown('''Um dos grandes fatores que influenciaram foi a coleta dos dados utilizados no treinamento do algoritmo, que foi feita de modo muito limitado devido ao uso da versão gratuita da **API**
    do **Twitter**, o que nos deixou com um **dataset** muito pequeno para o treinamento. Além disso, as palavras utilizadas no modelo são traduzidas, portanto, muitas palavras acabam por serem perdidas no meio do caminho,
    visto que várias delas são **gírias**, **abreviações** ou até **traduzidas erroneamente**, fazendo com que as mesmas sejam descartadas.''')
    st.markdown('''Os resultados podem retornar valores **0** ou **1**, sendo, respectivamente, **não** identificado com sintomas depressivos e **identificado** 
    com sintomas depressivos''')
    st.markdown('''**OBS:** Vale lembrar que o resultado não é oficial, o sistema não substitui um profissional da saúde!''')
    st.markdown('----')

    username = st.text_input('Insira o usuário:')
    if (st.button('Executar algoritmo')):
        createSpaces()

        qtd_tweets = 6
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
            st.write('Isso pode levar um tempinho...')
            modelo = load_word_embedding()
        
            tweets_dataframe['texto_limpo'] = tweets_dataframe['texto'].apply(cleanText)
            axis_tweets_dataframe = tweets_dataframe.copy()
            axis_tweets_dataframe.index = range(1,len(axis_tweets_dataframe)+1)

            st.write('Aqui estão os seus tweets que coletamos para fazer a análise')
            st.write(axis_tweets_dataframe[['usuario','texto_limpo']].to_markdown())

            ## Traduzir o texto para inglês
            tweets_dataframe['texto_traduzido'] = tweets_dataframe['texto_limpo'].apply(lambda x: translate(x))
            axis_tweets_dataframe_translated = tweets_dataframe.copy()
            axis_tweets_dataframe_translated.index = range(1,len(axis_tweets_dataframe_translated)+1)

            createSpaces()
            st.markdown('*Traduzindo seus tweets...*')
            showProgressBar(0.001)

            st.write('Aqui estão os seus tweets traduzidos')
            st.write(axis_tweets_dataframe_translated[['usuario','texto_limpo', 'texto_traduzido']].to_markdown())

            createSpaces()    
            # Transformando as frases em tokens
            tweets_dataframe["texto_traduzido"] = [tknzr.tokenize(sentence) for sentence in tweets_dataframe["texto_traduzido"]]

            encoded_docs_arrays = convertTokens(tweets_dataframe["texto_traduzido"], modelo)

            tweets_dataframe['X'] = pd.Series(encoded_docs_arrays)
            X = np.dstack(tweets_dataframe['X'].values).transpose(2,0,1)
            X = torch.FloatTensor(X)

            # Carregando o modelo
            st.markdown('*Carregando o modelo classificador de emoções...*')
            showProgressBar()
            model = torch.load(cwd+"/models/emotions_classifier_with_lasers_on_asteroids_50D.pth", map_location=torch.device('cpu'))
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

            tweets_dataframe['texto_limpo'] = tweets_dataframe['texto'].apply(breakPlotTitle)

            st.write('Aqui está os gráficos das distribuições das emoções que o nosso modelo classificou')
            fig, ax = plt.subplots(nrows=len(tweets_dataframe),ncols=1,figsize=(14, 14))

            for i, array in enumerate(preds_probs):   
                ax[i].set_title(tweets_dataframe['texto_limpo'][i])
                ax[i].bar(x=emotions, height=array, color=['lightcoral', 'khaki', 'bisque', 'lightsteelblue', 'lightgreen', 'thistle'])
            
            fig.tight_layout(pad=3.0)
            plt.subplots_adjust(hspace=6)
            st.pyplot(fig)

            createSpaces()

            st.write('Agora estamos carregando o modelo classificador de depressão')
            showProgressBar()
            createSpaces()

            # Preparando as emoções pro modelo de depressão
            modelDepression = torch.load(cwd+"/models/depression_detection.pth", map_location=torch.device('cpu'))
            modelDepression.eval()

            X_depression = []
            tweets_left = min_depression_tweets - len(preds)
            X_depression.append([[-1.79175947, -1.79175947, -1.79175947, -1.79175947, -1.79175947, -1.79175947]]*tweets_left+preds.tolist())
            X_depression = np.array(X_depression)
            X_depression = torch.FloatTensor(X_depression)

            st.write('Agora estamos analisando os seus tweets...')
            showProgressBar()
            createSpaces()

            predsDepression = modelDepression.forward(X_depression)
            predsDepression = predsDepression.detach().cpu().numpy()

            if predsDepression[0] == 1:
                st.markdown('E o resultado foi... **1** - nosso modelo identificou sinais de depressão em seus tweets')
            else:    
                st.markdown('E o resultado foi... **0** - nosso modelo não identificou sinais de depressão em seus tweets')
            
            st.markdown('**OBS:** Vale ressaltar que esta análise NÃO é oficial, a plataforma NÃO substitui, de qualquer forma, qualquer profissional da saúde para dar esta informação para você!')
            st.write('Independente do resultado, encorajamos a procura de ajuda profissional')
    
        else:
            st.write('Desculpe, não conseguimos utilizar os tweets deste usuário para fazer a análise :(')
            st.write('''Certifique-se de que o usuário possui, no mínimo, 3 tweets públicos, que ele não esteja 
                    com a conta no modo privado e que o mesmo possui tweets que não sejam: menções, retweets, 
                    que não contenha imagens ou vídeos e que não contenha links de forma geral.''')
            
            createSpaces()

            st.markdown('''**Importante:** Mesmo que o usuário altere a conta do modo privado, ele deverá
                        ter realizado algum tweet com a conta já publica para que o mesmo possa ser
                        coletado!''')

@st.cache
def load_model():
    cloud_model_location = '1j8mz4XDb9ydyNEqK-tmgHMEp4fvbXh4d'
    # save_dest = Path(cwd+f'/eda/data/gloVePath/')
    # save_dest.mkdir(exist_ok=True)
    
    f_checkpoint = Path(cwd+f'/eda/data/glove.6B.50d_word2vec.txt')

    if not f_checkpoint.exists():
        with st.spinner("Baixando modelo... isso pode levar um tempo! \n Por favor não interrompa"):
            from file_download import download_file_from_google_drive
            download_file_from_google_drive(cloud_model_location, f_checkpoint)
    
    return f_checkpoint

@st.cache()
def load_word_embedding():
    '''
    Carrega o arquivo GloVE de word embedding
    '''
    ## -------- Caso o arquivo já exista na pasta, deixar comentado --------
    # data_path = Path(cwd+f'/eda/data/newData/glove.6B.{50}d.txt')
   

    # if not data_path.exists():
    #     glove_file = datapath(load_model())
    # else:  
    #     glove_file = datapath(cwd+f'/eda/data/glove.6B.{50}d.txt')

    # tmp_file   = get_tmpfile(cwd+f"/eda/data/newData/glove.6B.{50}d_word2vec.txt")
    # _          = glove2word2vec(glove_file, tmp_file)

    # filename_txt = cwd+f"/eda/data/newData/glove.6B.50d_word2vec.txt"
    response = KeyedVectors.load_word2vec_format(load_model())
    return response


if __name__ == '__main__':
    main()


