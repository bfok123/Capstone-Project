import lyricsgenius
genius = lyricsgenius.Genius("_C9-biya5mg0NgX-DaYQMc9uNpvsIho2Z_86ngRT_6NLZ0FzzKCuNKyeVtE4G1OR")

genius.verbose = False # Turn off status messages
genius.remove_section_headers = False # Remove section headers (e.g. [Chorus]) from lyrics when searching
genius.skip_non_songs = True # Include hits thought to be non-songs (e.g. track lists)
genius.excluded_terms = ["(Remix)", "(Live)"] # Exclude songs with these words in their title

file = open("country_lyrics.txt", 'w')
file.write('')
file = open("country_lyrics.txt", 'a')

artists = ['Lizzo', 'Katy Perry', 'Imagine Dragons', 'Lady Gaga', 'Maroon 5', 'Camila Cabello', 'Sam Smith', '5 Seconds of Summer', 'Bruno Mars', 'Drake']
artists_country = ['Luke Combs', 'Dan + Shay', 'Kane Brown',
                   'Thomas Rhett', 'Florida Georgia Line',
                   'Chris Stapleton', 'Morgan Wallen',
                   'Maren Morris', 'Jason Aldean', 'Blake Shelton',
                   'Luke Bryan', 'Brett Young', 'Carrie Underwood',
                   'Jon Pardi', 'Zac Brown Band', 'George Strait',
                   'Old Dominion', 'Eric Church', 'Lee Brice',
                   'Kacey Musgraves', 'Kelsea Ballerini', 'Dierks Bentley',
                   'Blanco Brown', 'Jordan Davis', 'Tim McGraw', 'Chris Lane',
                   'Cody Johnson', 'Mitchell Tenpenny' , 'Chase Rice',
                   'Russell Dickerson']
artists_hiphop = ['Khalid', 'Drake', 'Lil Nas X', 'Travis Scott',
                  'Juice WRLD', 'DaBaby', 'Cardi B', 'Lil Baby',
                  'Meek Mill', 'A Boogie Wit da Hoodie',
                  'Lizzo', '21 Savage', 'XXXTENTACION',
                  'Chris Brown', 'Kodak Black', 'Gunna',
                  'J. Cole', 'Young Thug', 'Lil Tecca',
                  'YoungBoy Never Broke Again']
artists_minecraft = ['MineCraft Awesome Parodys', 'ReptileLegit',
                     'CaptainSparklez', 'TryHardNinja',
                     'BebopVox', 'Brad Knauber']
for artist_name in artists_country:
	artist = genius.search_artist(artist_name, max_songs=40)
	for song in artist.songs:
		try:
			file.write(song.lyrics)
			file.write("\n\n")
		except:
			continue
