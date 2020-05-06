#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Phyme import Phyme
import string

ph = Phyme()




def doTheyRhyme(word1, word2):

    rhyme_list = []

    for v in (ph.get_perfect_rhymes(word1).values()):
        rhyme_list = rhyme_list + v

    for v in (ph.get_family_rhymes(word1).values()):
        rhyme_list = rhyme_list + v

    for v in (ph.get_partner_rhymes(word1).values()):
        rhyme_list = rhyme_list + v

#     for v in (ph.get_additive_rhymes(word1).values()):
#         rhyme_list = rhyme_list + v

#     for v in (ph.get_subtractive_rhymes(word1).values()):
#         rhyme_list = rhyme_list + v

    #print(rhyme_list)

    if (word2 in rhyme_list and word2 != word1):
        return True
    else:
        return False


# In[26]:



#input: list of lines from a song
#output: number of lines that rhyme with each out
def howManyRhymes(lyrics):
    count = 0
    listOfLastWords = []

    #Generate of list of last words from each line
    for line in lyrics:
        wordsInLine = line.split()
        remove_punc = ""
        wordsInLine[-1] = wordsInLine[-1].lower()
        #remove puncuation
        for c in wordsInLine[-1]:
            if ord(c) >= 97 and ord(c) <= 122:
                remove_punc += c

        #only add words (remove any empty strings)
        if remove_punc != "":
            listOfLastWords.append(remove_punc)
#         print("line ending = " + remove_punc)


    #Loop through and count rhymes
    prev_word = listOfLastWords[0]
    already_rhymed = False
    for i in range(1, len(listOfLastWords)):
        curr_word = listOfLastWords[i]
        if (doTheyRhyme(curr_word, prev_word)):
            if (already_rhymed):
                count = count + 1
            else:
                count = count + 2
                already_rhymed = True
        else:
            prev_word = curr_word
            already_rhymed = False


    return count


# In[12]:
if (doTheyRhyme("me", "me")):
    print("yes")
