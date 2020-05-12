import lyricsgenius
genius = lyricsgenius.Genius("_C9-biya5mg0NgX-DaYQMc9uNpvsIho2Z_86ngRT_6NLZ0FzzKCuNKyeVtE4G1OR")

genius.verbose = False # Turn off status messages
genius.remove_section_headers = False # Remove section headers (e.g. [Chorus]) from lyrics when searching
genius.skip_non_songs = True # Include hits thought to be non-songs (e.g. track lists)
genius.excluded_terms = ["(Remix)", "(Live)"] # Exclude songs with these words in their title

file = open("sams_actually_generating_lyrics.txt", 'w')
file.write('')
file = open("sams_actually_generating_lyrics.txt", 'a')

artists = ['Lizzo', 'Katy Perry', 'Imagine Dragons', 'Lady Gaga', 'Maroon 5', 'Camila Cabello', 'Sam Smith', '5 Seconds of Summer', 'Bruno Mars', 'Drake']
for artist_name in artists:
	artist = genius.search_artist(artist_name, max_songs=20)
	for song in artist.songs:
		try:
			file.write(song.lyrics)
			file.write("\n\n")
		except:
			continue
