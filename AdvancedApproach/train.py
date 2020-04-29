import json 
from textgenrnn import textgenrnn

f = open('sections.json')
data = json.load(f)
batchsize = 2048
#%%
intro_gen = textgenrnn(name="intro_model")
intro_gen.train_on_texts(data['Intro'], word_level=True, num_epochs=50, gen_epochs=10, batch_size=batchsize)
#%%
#intro_gen.generate_samples(temperatures=[1.0, .9, .8, .7, .6, .5], max_gen_length=30)

#%%
chorus_gen = textgenrnn(name="chorus_model")
chorus_gen.train_on_text(data['Chorus'], new_model=True, word_level=True, num_epochs=50, gen_epochs=10, batch_size=batchsize)

verse_gen = textgenrnn(name="verse_model")
verse_gen.train_on_text(data['Verse'], new_model=True, word_level=True, num_epochs=50, gen_epochs=10, batch_size=batchsize)

bridge_gen = textgenrnn(name="bridge_model")
bridge_gen.train_on_text(data['Bridge'], new_model=True, word_level=True, num_epochs=50, gen_epochs=10, batch_size=batchsize)

outro_gen = textgenrnn(name="outro_model")
outro_gen.train_on_text(data['Outro'], word_level=True, num_epochs=50, gen_epochs=10, batch_size=batchsize)