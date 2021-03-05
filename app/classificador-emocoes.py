import streamlit as st
import numpy as np
import pandas as pd

import time

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

user = st.text_input('Insira o usuário:')

## Botão de rodar algoritmo

if (st.button('Executar algoritmo')):
    # Alguns espaços
    empty = ['','']
    for x in empty:
        st.text(x)
    my_bar = st.progress(0)
    for percent_complete in range(500):
        time.sleep(0.1)
        my_bar.progress(percent_complete + 1)