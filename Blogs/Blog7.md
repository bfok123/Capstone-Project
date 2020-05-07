### BLOG 7 ###

**Due May 7:**  

Continue advanced solution attempt #1, run more experiments, do more error analysis, and sketch out the next action plan. 

https://www.ranker.com/list/best-pop-artists-2019/ranker-music

Summary

## New Dataset ##
Last week we split our original dataset into sections which reduced our datasets too much. The results from the new models were very bad besides the chorus model. This week we scraped ~1,600 additional songs off of Genius Lyrics from the top 40 pop artists of 2019. This increased the sizes of our datasets by 7-75x.
1,668 Intros  
58,457 Choruses  
28,069 Verses  
7,743 Bridge  
8,802 Outros  

We used the same 2-layer, 128-cell LSTM as last week but increased the dimensions of word embeddings to get better fluency. The size of the RNN is limited by hardware and the number of epochs is limited by time. nlpg00 disconnects us after a few hours of training so each model gets around 50 epochs of training.

## Rhyming Engineering ##
Last week, we used Phyme - a rhyming API, to post-process our generated lines. We grouped rhyming lines together, took in user input for the rhyming scheme (ex: "AABAAB"), and outputted the lines in the given format. 

The problem with this approach was that context was not preserved, because rhyming lines were often far away from each other in the generations. This week, we tried to combat this by changing our post-processing technique by still grouping rhyming lines together, but this time sorting the rhymes by the distance between their lines. Our thought was that, since lines closer together should be more coherent, then if we choose to output the rhyming lines that are closest together our output should be more coherent while maintaining rhyme.

## Examples ##

\[Intro\]  

\[Verse\]  

\[Rhyming Verse\]  
just give me to see it and nobody’s do  
if you scared, i know it’s what you  
look, we gon do what it have to tell who? do you know  
we livin like i’m livin’ without you  

\[Chorus\]  

\[Non-Rhyming Verse\]  
boy, would you get up to know you i know  
you’re always talking saying you want to  
stay every night that you fake you miss  
me all the that we feel print,  

\[Bridge\]  


\[Outro\]  


## Evaluation ##
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

To improve the quality of intro, verse, and bridge models, we plan on increasing the size of our datasets by downloading more song lyrics. We also plan on augmenting our datasets by  duplicating our current datasets to the end of themselves and shuffling. Some of the parameters we plan on iterating over are temperature (ie: "creativity" of the generations) such as different temperatures for individual words in the sequence and different word embedding dimensions for each model to make up for differently sized datasets. 

