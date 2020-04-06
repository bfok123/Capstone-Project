### BLOG 1 ###

**Team name**: Natural Little Ponies Fok Tan Wheelock (NLP FTW)    
**Team members**: Brandon Fok, Nelson Tan, Sam Wheelock  
**GitHub**: [Click Here](https://github.com/bfok123/Capstone-Project)

**Project Ideas**

**1. Citizenship (or some other kind) Chat Bot**  
Input: Answer to a citizenship question  
Output: Pass/Fail to the question or elaborating on the question if they don't understand or get it confused with something else  
Technique: Deep learning using data from crowd sourcing. Not sure where to find data on how ESL speakers talk to proctors other than having them talk to real life proctors.  
Initial Goal: Classify correct answers with >50% accuracy. This means the bot is doing better than randomly assigning pass/fail.  
Stretch Goal: Classify correct answers with >75% accuracy. Ideally, >90% but that seems very, very stretchy.  

**2. Meme Generator**  
Input: Format of a meme e.g. Drake meme, Arthur meme, Thanos meme   
Output: Meme in given format (top text, bottom text, text for each panel)  
Technique: Deep learning using meme generator dataset and/or reddit memes dataset. These datasets include the names of the formats and the captions.  
Initial Goal: Generate memes given a meme format  
Stretch Goal: Make a functional UI that allows users to choose a meme type to generate for them, scrape reddit for memes and collect upvotes

**3. Music Lyric Generation**  
Input: Song structure, topics and/or keywords for each part  
Output: Complete song with given structure and topics/keywords  
Technique: Deep learning using data from RhymeZone (or other rhyme database), MetroLyrics/Genius, etc.  
Initial Goal: Generate a poem that rhymes given topic  
Stretch Goal: Generate a complete song given structure and topics of each part  
We can scrape Genius Lyrics for lyrics based on artist, genre, or something else and train on that dataset. We can further partition a song by verse, chorus, and bridge to generate a full song in the popular 2 verse, 1 bridge, 3 chorus format. 
