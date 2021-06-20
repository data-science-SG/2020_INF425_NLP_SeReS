# Detecção Automática de Sintomas do Transtorno Depressivo em Usuários de Redes Sociais
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
Esse projeto demonstra o desenvolvimento de um modelo de machine learning de redes neurais para a detecção de sintomas do transtorno depressivo com base em um dataset contendo tweets de usuários, realizado com a utilização de Jupyters Notebook na linguagem Python.

## Índice

## Conteúdos
[01 - Coleta de Tweets](need the link)

[02 - Modelo de Classificação de Emoções](need the link)

[03 - Modelo de Detecção de Sinais de Transtorno Depressivo](need the link)

## Primeiro passo
Para se fazer uso do código são necessários os seguintes requisitos:
 - [Bibliotecas Python com suas respectivas versões](https://github.com/data-science-SG/2020_INF425_NLP_SeReS/blob/master/requirements.txt)
- Jupyters Notebook

## Instalação
Clone o repositório
```
git clone https://github.com/data-science-SG/2020_INF425_NLP_SeReS.git
```

## Coleta de Tweets
Como o dataset contém informações **sensíveis**, mesmo que de forma pública, consideramos melhor aquele que utilizar o código realizar sua própria coleta.

Assim, a primeira parte para poder fazer uso do modelo é realizar a coleta de tweets utilizando o **Tweepy**. O Tweepy faz uso de chaves para seu uso, por isso é importante se criar uma conta no [Twitter Developer](https://developer.twitter.com/en).

Além disso, no terceiro notebook fazemos uso da biblioteca emot para conversão de emoticons para texto.

Mas caso tenha alguma dificuldade ou não queira criar a conta, você pode entrar em contato conosco para ter acesso a coleta feita por nós.

## Classicador de emoções
Para treinar o classificador de emoções é necessário rodar o notebook e exportar o modelo.
> Nota: O modelo de classicacação de emoções é treinado com a mescla de 2 datasets encontrados no Kaggle, com seus respectivos créditos.

## Modelo de Detecção de Sinais do Transtorno Depressivo
O último notebook é reservado para o treinamento do modelo final, para isso é necessário importar o dataset e o modelo de classificação de emoções

> Nota: Ambos os modelos possuem treinamento com base em hiperparametros que podem ser mudados ou adicionados. 

## Colaboradores
[Bruno Fontana](https://github.com/fontanads)
[Carlos Reinheimer](https://github.com/Carlos-Reinheimer)
[Eduarda Sorgetz](https://github.com/Sorgetz)



```diff
- adicionar resumo do projeto
```

## Como criar o dataset?


## Como funciona o modelo?


## Como treinar o modelo?

## Como utilizar o modelo pré-treinado?



## Contribuidores 

```diff
- fazer o bot do all-contributors funcionar
```

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/fontanads"><img src="https://avatars.githubusercontent.com/u/12212663?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Bruno Fontana</b></sub></a><br /><a href="https://github.com/data-science-SG/2020_INF425_NLP_SeReS/commits?author=fontanads" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!