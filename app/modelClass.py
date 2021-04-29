import torch
from torch import nn

class moodClassifierWithLasersOnSteroids(nn.Module):
  '''Modelo classificador de emoções com LSTMs.
  '''

  # ----------------------------------------------#
  # Método construtor
  def __init__(self, dim_embed, n_units_lstm, n_units_linear): 
    super().__init__()  

    embedding_seq = [] # 
    ann_seq       = [] # 
    soft_seq      = []

    #---------------------------------------------------------------#
    # Embedding step: sequência de operações para converter X --> h
    embedding_seq.append(nn.LSTM(input_size=dim_embed,
                                  hidden_size=n_units_lstm, 
                                  num_layers=1,
                                  batch_first=True))
    #---------------------------------------------------------------#

    #--------------------------------------------------------------------------#
    # ANN: Rede Neural Artifical Tradicional, com regressão logística na saída
    ann_seq.append(nn.Linear(n_units_lstm, n_units_linear))
    ann_seq.append(nn.ReLU(inplace=True))
    ann_seq.append(nn.Linear(n_units_linear, 6))
    
    #--------------------------------------------------------------------------#
    # Softmax :)
    soft_seq.append(nn.LogSoftmax(dim=1))

    #--------------------------------------------------------------------------#

    #--------------------------------------------------------------------------#
    # "merge" de todas as camamadas em uma layer sequencial 
    # (uma sequência para cada etapa)
    self.embedding = nn.Sequential(*embedding_seq)     # etapa de embedding 
    self.ann       = nn.Sequential(*ann_seq)           # etapa ANN
    self.soft      = nn.Sequential(*soft_seq)
    #--------------------------------------------------------------------------#


  def forward(self, x): 
    '''Processamento realizado ao chamar y=modelo(x)
    '''
    _, (x, _) = self.embedding(x)  # aplica a etapa de embedding
    x = x.transpose(1,0)   # inverte dimensões (força "batch first" no hidden state)
    x = self.ann(x)        # passa o embedding médio pelas camadas da ANN
    x = x.view(-1,6)
    x = self.soft(x)
    return x  