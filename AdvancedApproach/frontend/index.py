# -*- coding: utf-8 -*-
"""
Created on Thu May 14 16:50:05 2020

@author: Admin
"""

import tkinter as tk

window = tk.Tk()
window.title("Lyric Generator")
frame = tk.Frame()
pad = 5
var = tk.IntVar()
lbl_genre = tk.Label(window, text="Genre: ")
r_btn_pop = tk.Radiobutton(window, text="Pop", variable=var, value=0)
r_btn_hiphop = tk.Radiobutton(window, text="Hip Hop", variable=var, value=1)
r_btn_country = tk.Radiobutton(window, text="Country", variable=var, value=2)
r_btn_minecraft = tk.Radiobutton(window, text="Minecraft", variable=var, value=3)
btn_gen = tk.Button(window, text="Generate")
lbl_topic = tk.Label(window, text="Topic: ")
entry_topic = tk.Entry(window, width=40)
text_gen = tk.Text(frame, width=50, state=tk.DISABLED)
scrollbar = tk.Scrollbar(frame, command=text_gen.yview)
text_gen['yscrollcommand'] = scrollbar.set

# GRID LAYOUT
lbl_genre.grid(column=0, row=0, padx=pad, pady=pad)
r_btn_pop.grid(column=1, row=0, padx=pad, pady=pad)
r_btn_hiphop.grid(column=2, row=0, padx=pad, pady=pad)
r_btn_country.grid(column=3, row=0, padx=pad, pady=pad)
r_btn_minecraft.grid(column=4, row=0, padx=pad, pady=pad)
lbl_topic.grid(column=0, row=1, padx=pad, pady=pad)
entry_topic.grid(column=1, row=1, columnspan=4, padx=pad, pady=pad, sticky=tk.W)
btn_gen.grid(column=0, row=2, columnspan=5, padx=pad, pady=pad)

frame.grid(columnspan=5, column=0, row=3, padx=pad, pady=pad)
text_gen.grid(column=0, row=0,  sticky="nsew")
scrollbar.grid(column=1, row=0, sticky="nsew")

window.mainloop()
