# -*- coding: utf-8 -*-
"""
Created on Tue May  5 18:26:33 2020

@author: Nelson
"""
import os
import json

#%% load old json
save_loc = 'sections_minecraft.json'

current_dir = os.path.dirname(__file__)
with open(os.path.join(current_dir, save_loc)) as sections_file:
    sections = json.load(sections_file)

#%% append new data to json
with open(os.path.join(current_dir, 'minecraft_lyrics.txt')) as genius_songs:
    songs = genius_songs.readlines()
    
for i in range(len(songs)):
    for key in sections.keys():
        if key.lower() in songs[i].lower():
            i += 1
            section = ''
            while i < len(songs) and not songs[i].startswith('\n'):
                section += songs[i]
                i += 1
                sections[key].append(section)
            break
    i += 1
        

#%% write new data to json
with open(os.path.join(current_dir, save_loc), 'w') as f:
    json.dump(sections, f)
    
#%% check new json
save_loc= 'sections_hiphop.json'
with open(os.path.join(current_dir, save_loc)) as sections_file:
    checkjson = json.load(sections_file)
    
for key in checkjson.keys():
    print(key, len(checkjson[key]))