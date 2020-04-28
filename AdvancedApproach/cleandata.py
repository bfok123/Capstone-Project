# Gets rid of all columns except lyrics. Only keeps songs in English and in the pop genre.
# Separates by verse, chorus, bridge

#%%
from textgenrnn import textgenrnn
import pandas
import numpy as np
import re
from langdetect import detect, detect_langs

#%% remove unnecessary columns
data = pandas.read_csv('C:/Users/Admin/Desktop/Homework/Capstone-Project/Baseline Approach/lyrics.csv')
data = data[data.genre == 'Pop']
data = data.dropna()
data = data.drop(columns=["year", "genre", "artist", "index"])
data.to_csv('C:/Users/Admin/Desktop/Homework/Capstone-Project/AdvancedApproach/lyrics_clean.csv')

#%% remove non-english
to_remove = []
for idx, row in data.iterrows():
    lyrics = row['lyrics']
    try:
        if detect(lyrics) != 'en':
            to_remove.append(idx)
    except:
        to_remove.append(idx)
data = data.drop(to_remove)

#%% split lyrics into sections
sections = {}
sections['Chorus'] = []
sections['Verse'] = []
sections['Bridge'] = []
sections['Intro'] = []
sections['Outro'] = []
for idx, row in data.iterrows():
    lyrics = row['lyrics']
    curr_sections = re.findall('\[.*?\]', lyrics)
    if len(curr_sections) > 0: # song must be separated into sections
        for i in range(len(curr_sections) - 1): # separate sections and append to correct key
            match = ''
            for key in sections.keys():
                if key.lower() in curr_sections[i].lower():
                    match = key
            if match != '': # current section is valid, add to dict
                start = lyrics.find(curr_sections[i]) + len(curr_sections[i])
                end = lyrics.find(curr_sections[i + 1])
                sections[match].append(re.sub(r'[^\x00-\x7f]',r'', lyrics[start:end]))
                lyrics = lyrics[end:-1]
            else: # current section is invalid, skip to next section
                end = lyrics.find(curr_sections[i + 1])
                lyrics = lyrics[end:-1]
                
        # fencepost
        match = ''
        for key in sections.keys():
            if key.lower() in curr_sections[-1].lower():
                match = key
        if match != '':
            start = lyrics.find(curr_sections[-1]) + len(curr_sections[-1])
            end = -1
            sections[match].append(re.sub(r'[^\x00-\x7f]',r'', lyrics[start:end]))

            
#%% write to json
import json
import os

absolute_path = os.path.dirname(os.path.abspath(__file__))
path = absolute_path + "\\sections.json"

json = json.dumps(sections)
f = open(path,"w")
f.write(json)
f.close()

#%%
data.to_csv('C:/Users/Admin/Desktop/Homework/Capstone-Project/AdvancedApproach/lyrics_clean.csv')