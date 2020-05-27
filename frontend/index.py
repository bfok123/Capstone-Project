# -*- coding: utf-8 -*-
"""
Created on Thu May 14 16:50:05 2020

@author: Admin
"""

import tkinter as tk
import gen_lyrics

def onCheck(section):
    if section == 'intro':
        intro_rhyme.configure(state=(tk.DISABLED if var_intro.get() == 0 else tk.NORMAL))
    if section == 'verse':
        verse_rhyme.configure(state=(tk.DISABLED if var_verse.get() == 0 else tk.NORMAL))
    if section == 'chorus':
        chorus_rhyme.configure(state=(tk.DISABLED if var_chorus.get() == 0 else tk.NORMAL))
    if section == 'bridge':
        bridge_rhyme.configure(state=(tk.DISABLED if var_bridge.get() == 0 else tk.NORMAL))
    if section == 'outro':
        outro_rhyme.configure(state=(tk.DISABLED if var_outro.get() == 0 else tk.NORMAL))
        
def generate():
    genre = var.get()
    topic = entry_topic.get().lower()
    text_gen.configure(state=tk.NORMAL)
    text_gen.delete(1.0, tk.END)
    for key in section_vars:
        section_var = section_vars[key]
        if section_var.get() == 1:
            if genre not in models_by_genre.keys():
                models_by_genre[genre] = gen_lyrics.models(genre)
            model = models_by_genre[genre][key] # get textgenrnn object
            rhyme_scheme = section_rhymes[key].get().upper() # get rhyme scheme
            result = gen_lyrics.generateLyrics(model, rhyme_scheme, topic)
            text_gen.configure(state=tk.NORMAL)
            text_gen.insert(tk.END, '[' + key.capitalize() + ']\n')
            text_gen.insert(tk.END, result + '\n')
            text_gen.configure(state=tk.DISABLED)
    
    
print('loading pop model')
models_by_genre = {}
models_by_genre['pop'] = gen_lyrics.models('pop')
print('finished loading pop model')

window = tk.Tk()
window.title("Lyric Generator")
pad = 5

genre_frame = tk.Frame()
var = tk.StringVar() # radio button var
var.set('pop')
lbl_genre = tk.Label(genre_frame, text="Genre: ")
r_btn_pop = tk.Radiobutton(genre_frame, text="Pop", variable=var, value='pop')
r_btn_hiphop = tk.Radiobutton(genre_frame, text="Hip Hop", variable=var, value='hiphop')
r_btn_country = tk.Radiobutton(genre_frame, text="Country", variable=var, value='country')
r_btn_minecraft = tk.Radiobutton(genre_frame, text="Minecraft", variable=var, value='minecraft')

sections_frame = tk.Frame()
var_intro = tk.IntVar() # 1 means selected
var_verse = tk.IntVar()
var_chorus = tk.IntVar()
var_bridge = tk.IntVar()
var_outro = tk.IntVar()
section_vars = {'intro': var_intro, 'verse': var_verse, 'chorus': var_chorus, 'bridge': var_bridge, 'outro': var_outro}
lbl_sections = tk.Label(window, text="Sections to generate and rhyming scheme: ")
intro_rhyme = tk.Entry(sections_frame, state=tk.DISABLED)
verse_rhyme = tk.Entry(sections_frame, state=tk.DISABLED)
chorus_rhyme = tk.Entry(sections_frame, state=tk.DISABLED)
bridge_rhyme = tk.Entry(sections_frame, state=tk.DISABLED)
outro_rhyme = tk.Entry(sections_frame, state=tk.DISABLED)
section_rhymes = {'intro': intro_rhyme, 'verse': verse_rhyme, 'chorus': chorus_rhyme, 'bridge': bridge_rhyme, 'outro': outro_rhyme}
intro_section = tk.Checkbutton(sections_frame, text="Intro", variable=var_intro, command=lambda: onCheck('intro'))
verse_section = tk.Checkbutton(sections_frame, text="Verse", variable=var_verse, command=lambda: onCheck('verse'))
chorus_section = tk.Checkbutton(sections_frame, text="Chorus", variable=var_chorus, command=lambda: onCheck('chorus'))
bridge_section = tk.Checkbutton(sections_frame, text="Bridge", variable=var_bridge, command=lambda: onCheck('bridge'))
outro_section = tk.Checkbutton(sections_frame, text="Outro", variable=var_outro, command=lambda: onCheck('outro'))
lbl_ex = tk.Label(sections_frame, text="ex: AABB")

btn_gen = tk.Button(window, text="Generate", command=generate)

topic_frame = tk.Frame()
lbl_topic = tk.Label(topic_frame, text="Topic (Optional): ")
entry_topic = tk.Entry(topic_frame, width=20)

frame = tk.Frame() # generated text textbox and scrollbar
text_gen = tk.Text(frame, width=70, state=tk.DISABLED)
scrollbar = tk.Scrollbar(frame, command=text_gen.yview)
scrollbarx = tk.Scrollbar(frame, command=text_gen.xview, orient='horizontal')
text_gen['yscrollcommand'] = scrollbar.set
text_gen['xscrollcommand'] = scrollbarx.set

# GRID LAYOUT
genre_frame.grid(column=0, row=0, padx=pad, pady=pad, sticky=tk.W)
lbl_genre.grid(column=0, row=0, padx=pad, pady=pad)
r_btn_pop.grid(column=1, row=0, padx=pad, pady=pad)
r_btn_hiphop.grid(column=2, row=0, padx=pad, pady=pad)
r_btn_country.grid(column=3, row=0, padx=pad, pady=pad)
r_btn_minecraft.grid(column=4, row=0, padx=pad, pady=pad)

topic_frame.grid(column=0, row=1, padx=pad, pady=pad, sticky=tk.W)
lbl_topic.grid(column=0, row=0, padx=pad, pady=pad)
entry_topic.grid(column=1, row=0, padx=pad, pady=pad, sticky=tk.W)

lbl_sections.grid(column=0, row=2, pady=pad, padx=2 * pad, sticky=tk.W)

sections_frame.grid(column=0, row=3, pady=pad, padx=pad, sticky=tk.W)
intro_section.grid(column=0, row=0, pady=pad, padx=pad, sticky=tk.W)
intro_rhyme.grid(column=1, row=0, pady=pad, padx=pad)
lbl_ex.grid(column=2, row=0, pady=pad, padx=pad)
verse_section.grid(column=0, row=1, pady=pad, padx=pad, sticky=tk.W)
verse_rhyme.grid(column=1, row=1, pady=pad, padx=pad)
chorus_section.grid(column=0, row=2, pady=pad, padx=pad, sticky=tk.W)
chorus_rhyme.grid(column=1, row=2, pady=pad, padx=pad)
bridge_section.grid(column=0, row=3, pady=pad, padx=pad, sticky=tk.W)
bridge_rhyme.grid(column=1, row=3, pady=pad, padx=pad)
outro_section.grid(column=0, row=4, pady=pad, padx=pad, sticky=tk.W)
outro_rhyme.grid(column=1, row=4, pady=pad, padx=pad)

btn_gen.grid(column=0, row=4, padx=90, pady=pad, sticky="w")

frame.grid(column=0, row=5, padx=pad, pady=pad)
text_gen.grid(column=0, row=0, pady=pad, padx=pad, sticky="nsew")
scrollbar.grid(column=1, row=0, pady=pad, sticky="nsew")
scrollbarx.grid(column=0, row=1, padx=pad, sticky="nsew")

window.mainloop()
