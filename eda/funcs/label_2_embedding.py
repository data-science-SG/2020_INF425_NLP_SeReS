def label2Embedding(word, model):
  ''' Recebe uma string (word) e o modelo e devolve o embedding vector correspondente (se existir).
  '''
  if word in model.vocab:
    embed = model.get_vector(word)
    if embed is not None:
      return embed

# para testar a sua função
if __name__=='__main__':
  # código de teste das funções deste módulo
  label2Embedding('test')