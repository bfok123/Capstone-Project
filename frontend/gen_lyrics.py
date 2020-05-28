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
from itertools import zip_longest


# In[ ]:


def models(genre):
    
    models = {}
    
    file_prefix = '../AdvancedApproach/generator/'
    
    if genre != 'country':
        models['intro'] = textgenrnn(file_prefix + 'weights/' + genre + '/intro_model_weights.hdf5',
                                        vocab_path=file_prefix + 'weights/' + genre + '/intro_model_vocab.json',
                                        config_path=file_prefix + 'weights/' + genre + '/intro_model_config.json')

    models['chorus'] = textgenrnn(file_prefix + 'weights/' + genre + '/chorus_model_weights.hdf5',
                                    vocab_path=file_prefix + 'weights/' + genre + '/chorus_model_vocab.json',
                                    config_path=file_prefix + 'weights/' + genre + '/chorus_model_config.json')

    models['verse'] = textgenrnn(file_prefix + 'weights/' + genre + '/verse_model_weights.hdf5',
                                    vocab_path=file_prefix + 'weights/' + genre + '/verse_model_vocab.json',
                                    config_path=file_prefix + 'weights/' + genre + '/verse_model_config.json')

    models['bridge'] = textgenrnn(file_prefix + 'weights/' + genre + '/bridge_model_weights.hdf5',
                                    vocab_path=file_prefix + 'weights/' + genre + '/bridge_model_vocab.json',
                                    config_path=file_prefix + 'weights/' + genre + '/bridge_model_config.json')

    models['outro'] = textgenrnn(file_prefix + 'weights/' + genre + '/outro_model_weights.hdf5',
                                    vocab_path=file_prefix + 'weights/' + genre + '/outro_model_vocab.json',
                                    config_path=file_prefix + 'weights/' + genre + '/outro_model_config.json')
    
    return models


# In[118]:


#Input: model - used to generate more lines
#       rhyme_dict - dictionary to add rhymes to
#       num_generations - number of generations to make
#Output: dictionary where the keys are the rhymes and the values are a list of lines that rhyme
def add_more_rhymes(model, rhyme_dict, topic, num_generations, max_gen_length=50):

    lyrics = model.generate(num_generations, temperature=1.1, max_gen_length=max_gen_length, return_as_list=True, prefix=topic)
    
    lines = []
    for line in lyrics:
        split = line.splitlines()
        if (random.random() < 0.5):
            split.pop(0)
        for l in split:
            
            l = re.sub(r',|\(|\)|(chorus)|(verse 1 )|-|(intro)', '', l) # section garbage
            l = re.sub(r"'", " ", l)                                    # replaces apostrophes with spaces
            l = re.sub(r'\nt', '\n', l)                                 # replaces t at the beginning of lines with blank
            l = re.sub(r'(n\st\s|n\st$|n\st\n)', 'n\'t ', l)            # replaces "n t " with  "n't"
            l = re.sub(r'(\st\s|\st$|\st\n)', ' ', l)                   # replaces " t " with blank
            l = re.sub(r'(\sm\s|\sm$|\sm\n)', '\'m ', l)                # replaces " m " with "'m"
            l = re.sub(r'(\ss\s|\ss$|\ss\n)', '\'s ', l)                # replaces " s " with "'s"
            l = re.sub(r'(\se\s|\se$|\se\n)', ' ', l)                   # replaces " e " with " "
            l = re.sub(r'(\sb\s|\sb$|\sb\n)', ' ', l)                   # replaces " b " with " "
            l = re.sub(r'"', ' ', l)                                    # replaces '"' with " "
            words = l.split()

            words = [i for i, j in zip_longest(words, words[1:]) if i != j]

            if (len(words) > 1):
                lines.append(" ".join(words))

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
def generateLyrics(model, rhyme_scheme, topic, max_gen_length=50):
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
    add_more_rhymes(model, rhyme_dictionary, topic, 1, max_gen_length)
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
            
        add_more_rhymes(model, rhyme_dictionary, topic, 1, max_gen_length)

    # rhyme_dictionary -> list of lists -> sort by length of each list in reverse order
    rhyme_lists = []
    for rhyme in rhyme_dictionary.keys():
        rhyme_lists.append(rhyme_dictionary[rhyme])
    rhyme_lists = sorted(rhyme_lists, key=lambda rhyme_list: len(rhyme_list), reverse=True)
    
    # switch keys and values in rhyme_counts - ie: map rhyme to count to rhyme letter
    count_to_rhymes = dict()
    for letter in rhyme_counts.keys():
        if (rhyme_counts[letter] not in count_to_rhymes):
            count_to_rhymes[rhyme_counts[letter]] = []
        count_to_rhymes[rhyme_counts[letter]].append(letter)
        
    # sort rhyme counts
    rhyme_counts_list = sorted(list(rhyme_counts.values()), reverse=True)
    
    # map each letter/section of the rhyming scheme to a rhyme in rhyme_dict
    letter_to_rhyme = dict()
    for i in range(len(rhyme_counts_list)):
        curr_letter = count_to_rhymes[rhyme_counts_list[i]].pop()
        letter_to_rhyme[curr_letter] = rhyme_lists[i]     
        
        
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