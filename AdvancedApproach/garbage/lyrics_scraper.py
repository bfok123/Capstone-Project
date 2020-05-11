import lyricsgenius
import re
genius = lyricsgenius.Genius("_C9-biya5mg0NgX-DaYQMc9uNpvsIho2Z_86ngRT_6NLZ0FzzKCuNKyeVtE4G1OR")
genius.verbose = True
artists = ['Ariana Grande', 'Billie Eilish', 'Khalid', 'Post Malone', 'Imagine Dragons',
           'Halsey', 'Selena Gomez', 'Bruno Mars', 'Dua Lipa', 'Shawn Mendes', 'Panic! at the Disco',
           'Lady Gaga', 'Rihanna', 'Adele', 'The Chainsmokers', 'Katy Perry',
           'Beyonce', 'Charlie Puth', 'Sam Smith', 'Cardi B', '5 second of Summer',
           'The Weeknd', 'Bebe Rexha', 'Lizzo', 'Maroon 5', 'Sia', 'John Legend',
           'Ava Max', 'Alec Benjamin', 'Miley Cyrus', 'Niall Horna', 'Ellie Goulding',
           'Justin Timberlake', 'Sabrina Carpenter', 'Grace VanderWaal', 'Normani',
           'Lauv', 'OneRepublic', 'Hailee Steinfeld', 'Zara Larsson', 'Lana Del Rey',
           'Bazzi', 'Backstreet Boys', 'Jennifer Lopez', 'Charli XCX']
f = open("C:/Users/Admin/Desktop/Homework/Capstone-Project/AdvancedApproach/genius_songs.txt", "w")
f = open("C:/Users/Admin/Desktop/Homework/Capstone-Project/AdvancedApproach/genius_songs.txt", "a")

for artist_name in artists:
    artist = genius.search_artist(artist_name, max_songs=40)
    for song in artist.songs:
        lyrics = re.sub(r'[^\x00-\x7f]',r'',song.lyrics)
        f.write(lyrics)
f.close()