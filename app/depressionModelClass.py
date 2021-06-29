from torch import nn

class depression_detection(nn.Module):
  '''
  Modelo classificador de emoções
  '''
  # ----------------------------------------------#
  # Método construtor
  def __init__(self, n_in, num_layers, num_units, n_units_lstm, dim_lstm): 

    super().__init__()  
    ann_seq       = [] 
    lstm_seq      = []

    #--------------------------------------------------------------------------#
    # LSTM: 
    lstm_seq.append(nn.LSTM(input_size=dim_lstm, hidden_size=n_units_lstm, 
                                  num_layers=1, batch_first=True))
    #--------------------------------------------------------------------------#
    # ANN: Rede Neural Artifical Tradicional, com regressão logística na saída
    for i in range(1, num_layers):
      ann_seq.append(nn.Linear(in_features=num_units[i-1], out_features=num_units[i]))
      ann_seq.append(nn.ReLU(inplace=True))
    ann_seq.append(nn.Linear(in_features=num_units[-1], out_features=1))
    ann_seq.append(nn.Sigmoid())
    
    #--------------------------------------------------------------------------#
    # "merge" de todas as camamadas em uma layer sequencial 
    # (uma sequência para cada etapa)
    self.ann= nn.Sequential(*ann_seq)           # etapa ANN
    self.lstm_seq= nn.Sequential(*lstm_seq)     # etapa de lstm
    #--------------------------------------------------------------------------#

  def forward(self, x): 
    '''
    Processamento realizado ao chamar y=modelo(x)
    '''
    _, (x, _) = self.lstm_seq(x)  # aplica a etapa de embedding
    x = x.transpose(1,0)   # inverte dimensões (força "batch first" no hidden state)
    x = self.ann(x)        # passa o embedding médio pelas camadas da ANN
    x = x.view(x.shape[0],-1)
    return x