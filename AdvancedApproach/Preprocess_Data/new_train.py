import json 
from textgenrnn import textgenrnn

f = open('sections_week8.json')
data = json.load(f)
batchsize = 8192
rnn_size = 128
dim_embeddings = 100
max_words = 40000
gen_epochs = 25
#%%
"""print ('Training intro model')
intro_gen = textgenrnn(name="intro_model")
intro_gen.train_on_texts(data['Intro'],
                        new_model=True,
                        word_level=True,
                        num_epochs=50,
                        gen_epochs=gen_epochs,
                        rnn_size=rnn_size,
                        dim_embeddings=dim_embeddings,
                        max_words=max_words,
                        batch_size=batchsize)

print ('Training chorus model')
chorus_gen = textgenrnn(name="chorus_model")
chorus_gen.train_on_texts(data['Chorus'],
                          new_model=True,
                          word_level=True,
                          num_epochs=50,
                          gen_epochs=gen_epochs,
                          rnn_size=rnn_size,
                          dim_embeddings=dim_embeddings,
                          max_words=max_words,
                          batch_size=batchsize)
"""
print ('Training verse model')
verse_gen = textgenrnn(name="verse_model")
verse_gen.train_on_texts(data['Verse'],
                        new_model=True,
                        word_level=True,
                        num_epochs=50,
                        gen_epochs=gen_epochs,
                        rnn_size=rnn_size,
                        dim_embeddings=dim_embeddings,
                        max_words=max_words,
                        batch_size=batchsize)

print ('Training bridge model')
bridge_gen = textgenrnn(name="bridge_model")
bridge_gen.train_on_texts(data['Bridge'],
                          new_model=True,
                          word_level=True,
                          num_epochs=50,
                          gen_epochs=gen_epochs,
                          rnn_size=rnn_size,
                          dim_embeddings=dim_embeddings,
                          max_words=max_words,
                          batch_size=batchsize)

print ('Training outro model')
outro_gen = textgenrnn(name="outro_model")
outro_gen.train_on_texts(data['Outro'],
                         new_model=True,
                         word_level=True,
                         num_epochs=50,
                         gen_epochs=gen_epochs,
                         rnn_size=rnn_size,
                         dim_embeddings=dim_embeddings,
                         max_words=max_words,
                         batch_size=batchsize)
