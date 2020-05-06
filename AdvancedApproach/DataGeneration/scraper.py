import lyricsgenius
genius = lyricsgenius.Genius("qiXX9RC7I81FqTlF3W8fuZDwOsNIbNHWKGhVa-SwachyNpPWm18EmQfxDHsnS9o-")
artist = genius.search_artist("Andy Shauf", max_songs=3, sort="title")
print(artist.songs)
