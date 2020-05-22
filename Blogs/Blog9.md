### BLOG 9 ###

**Due May 21:**   

Datasets for other genres, streamlined rhyming post-processing, attached to frontend, topic support.

## New Datasets ##
We were happy with our pop dataset that we created by scraping Genius Lyrics last week so this week we gathered datasets for other genres, hip-hop, country, and Minecraft, like we planned in our project proposal. We scraped 40 songs from each of the 30 top artists of each genre in 2019 except for Minecraft which we could only find 6 high-profile artists on Genius Lyrics. Like the pop dataset, we split each of the other datasets into intros, verses, choruses, bridges, and outros.  
Breakdown of datasets:
| Pop                                                                     | Hip-hop                                                                | Country                                                               | Minecraft                                                         |
|-------------------------------------------------------------------------|------------------------------------------------------------------------|-----------------------------------------------------------------------|-------------------------------------------------------------------|
| Chorus 72631<br>Verse 52277<br>Intro 2955<br>Outro 7414<br>Bridge 10661 | Chorus 23804<br>Verse 41787<br>Intro 3383<br>Outro 2808<br>Bridge 1979 | Chorus 20798<br>Verse 12088<br>Intro 207<br>Outro 1835<br>Bridge 2413 | Chorus 1947<br>Verse 2014<br>Intro 157<br>Outro 150<br>Bridge 296 |

## Post-processing ##


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
with - - she - - me with  
the with  
ste be - - be  
in be  

\[Chorus\]  
so far, but can t do it all is enough  
roll with us  
and all the kings, had the things that i had high  
jet plane headed up to the sky (to the sky  

\[ Verse\]  
mix doors down down the people guy  
with used green come with come to i  
t and t about and t about  
i could i m the figureoutwhat t just t about  

\[Bridge\]  
oh you happily i,, know i  
make, dream that dream yes, i  
(hear this  
hear this  

\[Outro\]  
wanna no no under no  
bright diamond shine shine yeah yeah yeah oh  
and and  
paint face and and and and and and and and and and and and and and and paint and and and and and and 

## Evaluation ##

By just looking at the lines being produced, we can see that there are still some lines that make no sense, have bad punctuation, and repeat words way too often.  We will have to address this problem next week. Another problem with our model is that it is hard to evaluate the consistency of each model (how often they generate good results). This is an important part that we have not been addressing as we are not sure how to evaluate it. 

Despite the consistency problem with our model, we decided to use our survey to compare different methods of post processing.  We chose 3 different choruses (each constructed using a different post processing algorithm) that did not have obvious flaws (like repeated words).  One chorus was made using our normal rhyming algorithm, the next chorus was made using our strict rhyming algorithm, and the last chorus was made using no post processing at all.

After surveying 32 people, here are the averages we got:

|               | Fluency       | Coherency  | Does it Rhyme? | % that thought they were real |
| ------------- |---------------| -----------| ---------------| ------------------------------|
| **Original Rhyming Algorithm** |2.25|2.25|3.844|28.125%|
| **Strict Rhyming Algorithm**   |2.938|2.844|4.063|50%|
| **No Rhyming Algorithm**       |2.531|2.625|1.594|21.875%|
| **Real Chorus**                |3.875|4.094|2.469|90.625%|


(Side note: 90% of the people we surveyed listen to music often, 78% play or played an instrument, and 6% write their own lyrics)

## Planned Improvements ##
As we initially planned with this project, we plan on making a frontend UI for our model. It will allow the user to select a genre, input a topic, input rhymings schemes, and receive a complete song with the given options.

Also one of our initial goals with this project, we plan on gathering lyrics from different genres (ie: hip hop and country) using the Genius API in order to train more models on different genres. 

One of the problems that has been with us since the start is that some generations from our model repeat a word such as 'you' or 'the' many times one after the other. We plan on combatting this by setting a limit (2 or 3) on how many times a single word can repeat in one line. This should slightly improve the quality of our outputs.


