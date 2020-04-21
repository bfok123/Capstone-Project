#%%
from textgenrnn import textgenrnn
import pandas
import numpy as np
import re
from langdetect import detect

#%%
data = pandas.read_csv('C:/Users/Admin/Desktop/Homework/Capstone-Project/Baseline Approach/lyrics.csv')
data = data[data.genre == 'Pop']
data = data.dropna()

to_remove = []
for idx, row in data.iterrows():
    lyrics = row['lyrics']
    try:
        if detect(lyrics) != 'en':
            to_remove.append(idx)
    except:
        to_remove.append(idx)
data = data.drop(to_remove)

for idx, row in data.iterrows():
    data.loc[idx ,'lyrics'] = data['lyrics'][idx].replace('\\n', '\n')
    data.loc[idx ,'lyrics'] = data['lyrics'][idx].replace('"b"', " ")
    data.loc[idx ,'lyrics'] = re.sub("[\[].*?[\]]", "", data['lyrics'][idx])
    data.loc[idx ,'lyrics'] = re.sub(r'[^\x00-\x7F]+', "", data['lyrics'][idx])
        
#%% write to csv
data.to_csv('C:/Users/Admin/Desktop/Homework/Capstone-Project/Baseline Approach/lyrics_clean.csv')
#%%
data = data.lyrics.to_numpy()
#%%

file = open('lyrics.txt', 'w')
file.write('')
file = open('lyrics.txt', 'a')
for i in range(1000):
    lyric = data[i]
    if (type(lyric) == float):
        continue
    lyric = str(lyric.encode('UTF-8'))
    lyric = lyric.replace('\\n', '\n')
    lyric = lyric.replace('"b"', " ")
    file.write(lyric)

#%%

textgen = textgenrnn()
textgen.train_from_file('lyrics.txt', num_epochs=1)
textgen.generate(1)

#%%

generation = textgen.generate(10)
print (generation)

#%%

from textgenrnn import textgenrnn
textgen_2 = textgenrnn('textgenrnn_weights.hdf5')
textgen_2.generate(10, temperature=1.0)

#%%


