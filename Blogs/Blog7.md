### BLOG 7 ###

**Due May 7:**  

Continue advanced solution attempt #1, run more experiments, do more error analysis, and sketch out the next action plan. 



Summary

## New Dataset ##
Last week we split our original dataset into sections which reduced our datasets too much. The results from the new models were very bad besides the chorus model. This week we scraped ~1,600 additional songs off of Genius Lyrics from the top 40 pop artists of 2019 [Ranking](https://www.ranker.com/list/best-pop-artists-2019/ranker-music). This increased the sizes of our datasets by 7-75x.
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
gente de de de de lo mejor de
me
let s have some is sick your a the your i on disco s let a
lights stop the guess the and young see
and try i see
the rip it might another out the

\[Rhyming Verse\]  
just give me to see it and nobody’s do  
if you scared, i know it’s what you  
look, we gon do what it have to tell who? do you know  
we livin like i’m livin’ without you  

\[Chorus\]  
got that song is look up back
look up praise that
naw a heart and lay
(got that
look that i turn up chorus get to fad
all the stupid day,

\[Non-Rhyming Verse\]  
boy, would you get up to know you i know  
you’re always talking saying you want to  
stay every night that you fake you miss  
me all the that we feel print,  

\[Bridge\]  
just, you me t your a give and thing
same we thing
me door
it else your
my up all to safe, up fall

\[Outro\]  
How did I No longer?

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

Although our new rhyming technique slightly improved our output, there is still a lack of coherency between lines. Our next idea to combat this is to be more strict in our post-processing. Specifically, we plan on forcing rhyming lines to be directly next to each other in order to be considered for output. This means that we probably have to generate more lines in order to find rhyming lines directly next to each other (so getting output would take longer), but the quality of the output should improve.

Another problem with our current model is that we often have output that doesn't make any sense (either grammatically or because of gibberish). To combat this, we plan on removing data from our original dataset, and only using the Genius API for lyrics. Our original dataset had a lot of bad data that we could not completely remove through automation, but we know that Genius API lyrics (especially for well-known Pop artists) will be very clean and already sectioned by Chorus, Verse, Bridge, Intro, Outro.
