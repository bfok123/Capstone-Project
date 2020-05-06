import lyricsgenius
import re
genius = lyricsgenius.Genius("_C9-biya5mg0NgX-DaYQMc9uNpvsIho2Z_86ngRT_6NLZ0FzzKCuNKyeVtE4G1OR")
genius.verbose = True
artists = ['Post Malone', 'Ariana Grande', 'Billie Eilish', 'Khalid', 
           'Ed Sheeran', 'Taylor Swift', 'Rihanna', 'Halsey', 'Jonas Brothers',
           'P!nk', 'Panic! At The Disco', 'Shawn Mendes', 'Lizzo', 'Katy Perry',
           'Imagine Dragons', 'Lady Gaga', 'Maroon 5', 'Camila Cabello', 
           'Sam Smith', '5 Seconds of Summer', 'Bruno Mars', 'Drake']
f = open("C:/Users/Admin/Desktop/Homework/Capstone-Project/AdvancedApproach/genius_songs.txt", "w")
f = open("C:/Users/Admin/Desktop/Homework/Capstone-Project/AdvancedApproach/genius_songs.txt", "a")
#%%
artist = genius.search_artist("Post Malone", max_songs=2)
print(artist.songs[0].lyrics)

#%%
for artist_name in artists:
    artist = genius.search_artist(artist_name, max_songs=2)
    for song in artist.songs:
        f.write(song.lyrics)
f.close()