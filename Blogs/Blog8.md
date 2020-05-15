### BLOG 8 ###

**Due May 14:**  

Second advanced solution attempt. What did you try? Are there any exciting results? Any confusing results? What are the failure modes? What will you try next?

Summary

## New Dataset ##
Last week we combined our original lyric datasets (sectioned by Chorus, Verse, etc.) with lyrics from the top 40 pop artists scraped with the Genius API. We had mixed results with this approach - while we did have some good generations, there were still many grammatical and spelling errors in most generations. This week, we decided to get rid of our original dataset, due to there being a lot of bad data, and we are now solely using Genius API for our lyric datasets. Genius API provides us with consistent formatting of the lyrics, in particular every song (for well-known artists) are sectioned by Chorus, Verse, Bridge, Intro, Outro as needed. We have had no problems with unicode characters or any other special characters with Genius API as well. Since we removed our original datasets, we added song lyrics from ~40 more artists to keep our datasets sufficiently large. Here are the sizes of our new datasets:

3,191 Intros  
83,928 Choruses  
54,373 Verses  
11,684 Bridge  
15,878 Outros  

## Rhyming Engineering ##
Last week, we continued to use Phyme - a rhyming API, to post-process our generated lines. We generated a bunch of lines, put rhyming lines together using Phyme, sorted the rhymes by the distance between lines, and outputted the result. However, our results from this approach weren't as good as we had hoped.

This week, we decided to make our rhyming algorithm even more strict, by forcing our outputted rhyming lines to be right next to each other in the generation. Since lines that are directly next to each other in the initial generation will have the most consistency in terms of context, we wanted to take full advantage of this in order to improve the quality of our output. The results, which you can see in the 'Examples' section below, were slightly better than before.

## Song Topics ##
One of our intial goals for this project was to allow users to input a topic for the generation and get back a song that revolves around the given topic. Our current idea to do this is to use the ```prefix``` input that our model can take in for generation, and have the model do text completion based on the ```prefix```. Since we are using an RNN model with Attention, our idea is that the context from the prefix should hold throughout the generation and act as a 'topic' for our output. Here are some examples using this idea:

## Examples ##

\[Intro\]  

\[Rhyming Verse\]  

\[Chorus\]  

\[Non-Rhyming Verse\]  

\[Bridge\]  

\[Outro\]  

## Evaluation ##
Overall, the quality of generated lyrics for each section except for chorus was better. Our chorus model kept plagiarizing actual choruses and the ones that were not plagiarized did not sound as good as last week. This might be because the chorus data has many duplicates and isn't shuffled so certain words trigger plagiarization of several lines.

Using our evaluation survey, we pitted last week's generated chorus with P!NK's chorus in "Slut Like You". Our chorus scored lower in fluency and coherency and was able to trick 4/15 (26.7%) people into thinking our generated lyrics were real and P!NK's were fake.

\[Generated Lyrics\]  
From a left of dreams  
Even though it seems  
To pretend as crazy i can see  
From a left of dreams  
Even though it seems  
There’s nothing left to me  

2.8 - Fluency  
2.67 - Coherency  
N/A - Topic  
4.27 - Does it rhyme?  

\[Chorus from Slut Like You\]  
I got a little piece of you-hoo  
And it's just like woohoo  
Wham, bam, thank you, ma'am!  
Woohoo  
You say you're looking for a foo-ool  
And I'm just like me, too  
I'm gonna let ya know the truth  

3.53 - Fluency  
3.53 - Coherency  
N/A - Topic  
4 - Does it rhyme?  

## Planned Improvements ##
frontend

more genres

set limit on how many times a word can repeat in one line
