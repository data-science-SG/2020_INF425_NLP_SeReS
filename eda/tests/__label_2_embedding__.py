def label2Embedding(sentence):
    """ Check if the word of the received sentence is included in the pre-trained word embedding and return it's embedding

    Keywords arguments:
    sentence -- tweet itself
    """
  for word in sentence: 
    if word in embedding.vocab:
      embed = embedding.get_vector(word)
      return embed
    else:
      print("This word is not in the vocabuylary: ", word, "\n")