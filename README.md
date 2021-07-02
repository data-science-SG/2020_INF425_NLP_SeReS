<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-3-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

# 🎭 Detecção Automática de Sintomas do Transtorno Depressivo em Usuários de Redes Sociais
Esse projeto demonstra o desenvolvimento de um modelo de machine learning de redes neurais para a detecção de sintomas do transtorno depressivo com base em um dataset contendo tweets de usuários, realizado com a utilização de Jupyters Notebook na linguagem Python.

## 📑 Índice
[Conteúdos](##conteúdos)
[Primeiros Passos](##primeiros-passos)
[Instalação](##intalacao)
[Coleta de Tweets](##coleta-de-tweets)
[Classificador de Emoções](##classificador-de-emocoes)
[Modelo de Detecção de Sinais do Transtorno Depressivo](##modelo-de-deteccao-de-sintomas-do-transtorno-depressivo)
[Streamlit](##streamlit)

## Conteúdos
[01 - Coleta de Tweets](https://github.com/Sorgetz)
[02 - Modelo de Classificação de Emoções](https://github.com/Sorgetz)
[03 - Modelo de Detecção de Sinais de Transtorno Depressivo](https://github.com/Sorgetz)

## Primeiros passos
Para se fazer uso do código são necessários os seguintes requisitos:
 - [Bibliotecas Python com suas respectivas versões](https://github.com/data-science-SG/2020_INF425_NLP_SeReS/blob/master/requirements.txt)
- Jupyters Notebook

## 📥 Instalação
Clone o repositório
```
git clone https://github.com/data-science-SG/2020_INF425_NLP_SeReS.git
```

## 💬 Coleta de Tweets
Como o dataset contém informações **sensíveis**, mesmo que de forma pública, consideramos melhor aquele que utilizar o código realizar sua própria coleta.

Assim, a primeira parte para poder fazer uso do modelo é realizar a coleta de tweets utilizando o **Tweepy**. O Tweepy faz uso de chaves para seu uso, por isso é importante se criar uma conta no [Twitter Developer](https://developer.twitter.com/en).

```python
access_token = 'Insira seu acess token'
access_token_secret = 'Insira seu acess token secret'

API_key = 'Insira consumer key'
API_secret_key = 'Insira consumer secret'
```
Além disso, no terceiro notebook fazemos uso da biblioteca emot para conversão de emoticons para texto.

Mas caso tenha alguma dificuldade ou não queira criar a conta, você pode entrar em contato conosco para ter acesso a coleta feita por nós.

Caso deseje modificar alguns parâmetros de coleta, eles podem ser modificados nestas linhas.
```python
#Escolhendo a quantidade de tweets
num_itens_depre = 600
num_itens_sad = 10

#Quantos tweets do usuário coletar
num_tweets_depre = 10
num_tweets_sad = 4

#Mínimo de tweets que o usuário deve ter para entrar no dataset
min_tweets = 3
```

Além disso, infelizmente os tweets deve passar por um filtro manual, para retirar ironias e falsos-positivos.

## 📊 Classicador de emoções
![image](https://drive.google.com/uc?export=view&id=1kziSBU95NhBx3kxw-oKXhHPmgvsG2fNx) 

Para treinar o classificador de emoções é necessário rodar o notebook e exportar o modelo.
> Nota: O modelo de classicacação de emoções é treinado com a mescla de 2 datasets encontrados no Kaggle, com seus respectivos créditos nos cadernos.

![image](https://drive.google.com/uc?export=view&id=1SR-phh2X58VvbhrSVNKy1_KnkFzQt0Gu)

## Modelo de Detecção de Sinais do Transtorno Depressivo
O último notebook é reservado para o treinamento do modelo final, para isso é necessário importar o dataset e o modelo de classificação de emoções

> Nota: Ambos os modelos possuem treinamento com base em hiperparametros que podem ser mudados ou adicionados. 

## Streamlit
Caso deseje ver o código em ação sem precisar glonar o repositório você pode acessar o nosso Streamlit no seguinte link: [Inserir link]

## Autores

Feito com ❤️ por Bruno Fontana, Carlos Reinheimer e Eduarda Sorgetz. Entre em contato!
 ![Linkedin Badge](https://img.shields.io/badge/-Bruno-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/fontanads/)   ![Linkedin Badge](https://img.shields.io/badge/-Carlos-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/carlos-reinheimer-108227199/)   ![Linkedin Badge](https://img.shields.io/badge/-Eduarda-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/eduarda-sorgetz-2690981a4/) 

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/fontanads"><img src="https://avatars.githubusercontent.com/u/12212663?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Bruno Fontana</b></sub></a><br /><a href="https://github.com/data-science-SG/2020_INF425_NLP_SeReS/commits?author=fontanads" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/Carlos-Reinheimer"><img src="https://avatars.githubusercontent.com/u/49253291?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Carlos-Reinheimer</b></sub></a><br /><a href="https://github.com/data-science-SG/2020_INF425_NLP_SeReS/commits?author=Carlos-Reinheimer" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/Sorgetz"><img src="https://avatars.githubusercontent.com/u/53908201?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Sorgetz</b></sub></a><br /><a href="https://github.com/data-science-SG/2020_INF425_NLP_SeReS/commits?author=Sorgetz" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
