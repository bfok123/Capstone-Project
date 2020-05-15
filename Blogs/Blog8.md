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
Last week, we continued to use Phyme - a rhyming API, to post-process our generated lines. We generated a bunch of lines, put rhyming lines together using Phyme, sorted the rhymes by the distance between lines, and outputted the result. Our results were fine, but we thought that we could further improve our output's context.

This week, we decided to make our rhyming algorithm even more strict, by forcing our outputted rhyming lines to be right next to each other in the generation. Since lines that are directly next to each other in the initial generation will have the most consistency in terms of context, we wanted to take full advantage of this in order to improve the quality of our output. Unfortunately, this new approach did not work as well as we had hoped, as the chances of getting two rhyming lines directly next to each other in the initial generation is low so we needed to generate very many lines in order to get an output with reasonable length.

## Song Topics ##
One of our intial goals for this project was to allow users to input a topic for the generation and get back a song that revolves around the given topic. Our current idea to do this is to use the ```prefix``` input that our model can take in for generation, and have the model do text completion based on the ```prefix```. Since we are using an RNN model with Attention, our idea is that the context from the prefix should hold throughout the generation and act as a 'topic' for our output. Here are some examples using this idea:

## Examples ##

# No Rhyming #

\[Chorus\]
i think about you, baby
ill be your love, girl, know
maybe we can t have
sorry, i never hurt the pain you left danced
spread your wings as heaven there and good fade god

# Normal Rhyming #

\[Intro\]
hooked i on you you
fucked i went tired the understand tell do
ever people some i spreading to i
ladies i it my see my

\[Chorus\]
today back, no name
i just throw it stain to the heart that is heart is use to heal the pain
don t wanna wait on front, i won t lie
sudden half you, don t buy

\[Verse\]
sink till baby you were high the dawn
don't a guy guy needs a song
and some money some nights of the tube and over and waiting too real show up
heads i m am but

\[Bridge\]
gonna and the and and you you
you the and and you
before his - his his getting his falling
middle night the away the it baby a the baby in too the the far baby, baby be dark from in in

\[Outro\]
worse can
and you
i until problem my in with goddamn
you you you

# Strict Rhyming #

\[Intro\]  

\[Rhyming Verse\]  

\[Chorus\]  

\[Non-Rhyming Verse\]  

\[Bridge\]  

\[Outro\]  

## Evaluation ##


## Planned Improvements ##
As we initially planned with this project, we plan on making a frontend UI for our model. It will allow the user to select a genre, input a topic, input rhymings schemes, and receive an a complete song with the given options.

Also one of our initial goals with this project, we plan on gathering lyrics from different genres using the Genius API in order to train more models on different genres. 

One of the problems that has been with us since the start is that some generations from our model repeat a word such as 'you' or 'the' many times one after the other. We plan on combatting this by setting a limit (2 or 3) on how many times a single word can repeat in one line. This should slightly improve the quality of our outputs.
