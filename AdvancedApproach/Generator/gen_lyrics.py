#!/usr/bin/env python
# coding: utf-8

# In[98]:


from textgenrnn import textgenrnn
import pandas
import numpy as np
import rhymes as r
import importlib
import string
import random
importlib.reload(r)
import re


# In[ ]:


def models(genre):
    
    models = []
    
    models.append(textgenrnn('weights/' + genre + '/intro_model_weights.hdf5',
                                    vocab_path='weights/' + genre + '/intro_model_vocab.json',
                                    config_path='weights/' + genre + '/intro_model_config.json'))

    models.append(textgenrnn('weights/' + genre + '/chorus_model_weights.hdf5',
                                    vocab_path='weights/' + genre + '/chorus_model_vocab.json',
                                    config_path='weights/' + genre + '/chorus_model_config.json'))

    models.append(textgenrnn('weights/' + genre + '/verse_model_weights.hdf5',
                                    vocab_path='weights/' + genre + '/verse_model_vocab.json',
                                    config_path='weights/' + genre + '/verse_model_config.json'))

    models.append(textgenrnn('weights/' + genre + '/bridge_model_weights.hdf5',
                                    vocab_path='weights/' + genre + '/bridge_model_vocab.json',
                                    config_path='weights/' + genre + '/bridge_model_config.json'))

    models.append(textgenrnn('weights/' + genre + '/outro_model_weights.hdf5',
                                    vocab_path='weights/' + genre + '/outro_model_vocab.json',
                                    config_path='weights/' + genre + '/outro_model_config.json'))
    
    return models


# In[118]:


#Input: model - used to generate more lines
#       rhyme_dict - dictionary to add rhymes to
#       num_generations - number of generations to make
#Output: dictionary where the keys are the rhymes and the values are a list of lines that rhyme
def add_more_rhymes(model, rhyme_dict, topic, num_generations):

    lyrics = model.generate(num_generations, temperature=1.1, max_gen_length=1000, return_as_list=True, prefix=topic)
    
    lines = []
    for line in lyrics:
        split = line.splitlines()
        if (random.random() < 0.5):
            split.pop(0)
        for l in split:
            
            l = re.sub(r',|\(|\)|(chorus)|(verse 1 )|-|(intro)', '', l)
            l = re.sub(r'\nt', '\n', l)
            l = re.sub(r'(n\st\s|n\st$|n\st\n)', 'n\'t ', l)
            l = re.sub(r'(\st\s|\st$|\st\n)', ' ', l)
            l = re.sub(r'(\sm\s|\sm$|\sm\n)', '\'m ', l)
            l = re.sub(r'(\ss\s|\ss$|\ss\n)', '\'s ', l)
            l = re.sub(r'(\se\s|\se$|\se\n)', ' ', l)
            l = re.sub(r'(\sb\s|\sb$|\sb\n)', ' ', l)
            words = l.split()

            prevword = ""
            duplicates = False
            for word in words:
                if word == prevword:
                    duplicates = True
                prevword = word

            if (len(words) > 1 and not duplicates):
                lines.append(l)

    #Generate of list of last words from each line
    for line in lines:
        if (len(line) == 0):
            continue
        try:
            wordsInLine = line.split()
            curr_word = ""
            wordsInLine[-1] = wordsInLine[-1].lower()
            #remove puncuation
            for c in wordsInLine[-1]:
                if ord(c) >= 97 and ord(c) <= 122:
                    curr_word += c
            #only add words (remove any empty strings)
            if curr_word != "":
                IT_RHYMES_BABYYY = False
                for key in rhyme_dict.keys():
                    if (r.doTheyRhyme(curr_word, key)):
                        rhyme_dict[key].append(line)
                        IT_RHYMES_BABYYY = True
                        #print("Adding", "[" + line + "]", "into the dictionary")
                if (not IT_RHYMES_BABYYY):
                    rhyme_dict[curr_word] = [line]
                    #print("Putting new rhyme", "[" + line + "]", "into the dictionary")
        except:
            continue


# In[119]:


#Input: genre - string describing the users requested genre
#       rhyme_scheme - string of capital letters detailing the rhyming scheme
def generateLyrics(model, rhyme_scheme, topic):
    # count the required number of lines for each letter/section of the rhyming scheme
    rhyme_counts = dict()
    lyrics_baby = ""
    for char in rhyme_scheme:
        if char in rhyme_counts:
            rhyme_counts[char] += 1
        else:
            rhyme_counts[char] = 1
    
    #Start by adding rhymes to our dictionary
    rhyme_dictionary = dict()
    add_more_rhymes(model, rhyme_dictionary, topic, 1)
    not_enough_rhymes = True

    #Keep adding rhymes until we have enough
    while not_enough_rhymes:
        required_rhyme_counts = []
        
        #Make a list of how many of each rhyme we need
        for letter in rhyme_counts.keys():
            required_rhyme_counts.append(rhyme_counts[letter])
            
        
        #build list of dictionary lengths        
        actual_rhyme_counts = []
        for value in rhyme_dictionary.values():
            actual_rhyme_counts.append(len(value))
        
        
        #Sort both lists
        required_rhyme_counts.sort(reverse=True)
        actual_rhyme_counts.sort(reverse=True)
        
        #Loop through required rhyme counts and see if the dictionary has enough rhymes for it
        #Otherwise add more rhymes
        for i in range(len(required_rhyme_counts)):
            if (i < len(actual_rhyme_counts)):
                if (i == len(required_rhyme_counts) - 1 and required_rhyme_counts[i] <= actual_rhyme_counts[i]):
                    not_enough_rhymes = False
                elif (not not not required_rhyme_counts[i] <= actual_rhyme_counts[i]):
                    break
        
        add_more_rhymes(model, rhyme_dictionary, topic, 1)

    # map each letter/section of the rhyming scheme to a rhyme in rhyme_dict
    used_rhymes = set()
    letter_to_rhyme = dict()
    for letter in rhyme_counts.keys():
        for rhyme in rhyme_dictionary.keys():
            # if the current rhyme has enough rhymes for the current letter in the rhyming scheme
            # AND the rhyme hasn't been used, use it
            if (len(rhyme_dictionary[rhyme]) >= rhyme_counts[letter] and rhyme not in used_rhymes):
                letter_to_rhyme[letter] = rhyme_dictionary[rhyme]
                used_rhymes.add(rhyme)
                break
    # print the results!
    rhyme_indices = dict()
    for char in rhyme_scheme:
        if (char not in rhyme_indices):
            lyrics_baby = lyrics_baby + letter_to_rhyme[char][0] + '\n'
            rhyme_indices[char] = 1
        else:
            lyrics_baby = lyrics_baby + letter_to_rhyme[char][rhyme_indices[char]] + '\n'
            rhyme_indices[char] += 1
            
    return lyrics_baby

