def label2Embedding(sentence):
  """ Check if the word of the received sentence is included in the pre-trained word embedding and return it's embedding
  
  Keywords arguments:
  sentence -- tweet itself
  """
  print('HELLO CARLOS')
  for word in sentence:
    if word in embedding.vocab:
      embed = embedding.get_vector(word)
      return embed
    else:
      print("This word is not in the vocabuylary: ", word, "\n")

# para testar a sua função
if __name__=='__main__':
  # código de teste das funções deste módulo
  label2Embedding('test')