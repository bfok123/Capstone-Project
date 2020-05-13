# -*- coding: utf-8 -*-
"""
Created on Wed May 13 15:23:35 2020

@author: Admin
"""

import os
import re
current_dir = os.path.dirname(__file__)

file = open(os.path.join(current_dir,'genius_songs.txt'), 'r')
filewrite = open('C:/Users/Admin/Desktop/Homework/Capstone-Project/AdvancedApproach/Preprocess_Data/genius_songs4.txt', 'w')
filewrite = open('C:/Users/Admin/Desktop/Homework/Capstone-Project/AdvancedApproach/Preprocess_Data/genius_songs4.txt', 'a')

keywords = {'[Intro', '[Verse', '[Chorus', '[Outro', '[Bridge'}

for line in file:
    line = re.sub(r'\([^()]*\)', '', line)
    flag = False
    for keyword in keywords:
        if keyword.lower() in line.lower():
            index = line.lower().index(keyword.lower())
            if index > 0:
                flag = True
                line1 = line[0:index]
                line2 = line[index:]
                filewrite.write(line1 + '\n\n')
                filewrite.write(line2)
            #endif
        #endif
    #endfor
    if not flag:
        filewrite.write(line)
    
    