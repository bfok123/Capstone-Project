from textgenrnn import textgenrnn
import pandas
import numpy as np
import rhymes

lines = []
dict_of_rhymes = dict()

def gen_lyrics() {

    word_level_model = textgenrnn('full_dataset_word_level.hdf5',
                                  vocab_path='word_level_vocab.json',
                                  config_path='word_level_config.json')

    lyrics = word_level_model.generate(1, temperature=1.0, max_gen_length=1000, return_as_list=True)

    lines = lyrics[0].splitlines()
}

def post_process() {

    rhyme_dict = dict()

    #Generate of list of last words from each line
    for index, line in enumerate(lines):
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
                    if (rhymes.doTheyRhyme(curr_word, key)):
                        rhyme_dict[key].append(index)
                        IT_RHYMES_BABYYY = True
                if (not IT_RHYMES_BABYYY):
                    rhyme_dict[curr_word] = [index]
        except:
            print (curr_word, ' was not found in the dictionary')
            continue

        dict_of_rhymes = rhyme_dict
}

def out1() {
    print ('What rhyming scheme would you like to use? (A to Z)')
    rhyme_scheme = input()
    if (not re.fullmatch('[A-Z]+', rhyme_scheme)):
        print ('That is not a valid rhyming scheme.')
        exit()

    # count the required number of lines for each letter/section of the rhyming scheme
    rhyme_counts = dict()
    for char in rhyme_scheme:
        if char in rhyme_counts:
            rhyme_counts[char] += 1
        else:
            rhyme_counts[char] = 1
    print (rhyme_counts)

    # map each letter/section of the rhyming scheme to a rhyme in rhyme_dict
    used_rhymes = set()
    letter_to_rhyme = dict()
    for letter in rhyme_counts.keys():
        for rhyme in rhyme_dict.keys():
            # if the current rhyme has enough rhymes for the current letter in the rhyming scheme
            # AND the rhyme hasn't been used, use it
            if (len(rhyme_dict[rhyme]) >= rhyme_counts[letter] and rhyme not in used_rhymes):
                letter_to_rhyme[letter] = rhyme_dict[rhyme]
                used_rhymes.add(rhyme)
                break

    print (letter_to_rhyme)

    # print the results!
    rhyme_indices = dict()
    for char in rhyme_scheme:
        if (char not in rhyme_indices):
            print (lines2[0])
            rhyme_indices[char] = 1
        else:
            print (lines2[letter_to_rhyme[char][rhyme_indices[char]]])
            rhyme_indices[char] += 1

}
