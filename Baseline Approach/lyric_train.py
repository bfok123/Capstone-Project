from textgenrnn import textgenrnn
import os

absolute_path = os.path.dirname(os.path.abspath(__file__))
file_path = absolute_path + '\\lyrics2.txt'

textgen = textgenrnn()
textgen.train_from_largetext_file(file_path, 
                                  num_epochs=50, 
                                  batch_size=2048, 
                                  max_words=35000,
                                  dim_embeddings=300)