### BLOG 6 ###

**Due April 30:**  

First advanced solution attempt. What did you try? Are there any exciting results? Any confusing results? What are the failure modes? What will you try next?

For this week we devoted a lot of time to engineering rhyming post-generation. We also wanted to see how a smaller, more focused dataset affected the quality of lyrics. 

## New Dataset ##
Last week we saw that there were sections of our generation that looked a lot like choruses when we rearranged the lines to put rhymes closer together. We wanted to test if this could happen naturally (no post-processing) so we trained a 2-layer, 128-cell LSTM for each section of each song, meaning we made 5 different models. The sections were labeled in some of the songs and we got a total of  

Chorus (7893), Verse (1270), Bridge (618), Intro (136), Outro (118) on 4,132 songs.  

Although this was a big step down from our original 36,000 songs, we thought that the quality of labeled songs was closer to what we wanted for output (popular songs are more likely to be labeled and we want the top pop songs) so the results would be comparable to the full dataset. 

Like the previous week, we generated sequences with beam search and with temperatures around 0.7, 0.8, and 0.9. Temperature affects the randomness of what's chosen by the beam search. A lower temperature (0.5) would choose the highest probability word everytime like "yeah, yeah, yeah, ..., yeah" and a higher temperature (1.0) would sometimes choose low probabilty words outputting more "creative" lyrics. 

We mostly left temperature alone this week because we were focusing on getting good rhyming engineering.

## Rhyming Engineering ##
We approached rhyming a few different ways. We would first generate a long list of lyrics, about 100 lines, then group them into lines that all rhymed with each other (using a python rhyming api and a python dictionary). This was important to take advantage of attention (longer memory of previous generated words) to achieve coherency between lines. We would then use user input to order the rhymes.

For example, user input: "AABB" would print 4 lines (one for each letter) where lines labelled with the same uppercase character would rhyme with each other. Using this input along with our list of rhyming lines, our last step was to pick which rhyming lines to use for the final lyrics. As of right now, we are randomly picking lines that fit the users format.  However in the future we will experiment by choosing rhymes based on their frequency, minimum distance between lines, and the average distance between lines.  We want to try choosing based off of the minimum distance between the rhyming lines because the model generates based off of the context, so theoretically lines that are generated closer together should be more coherent.

## Examples ##

\[Intro\]
on  
dig on well we the on  
i know about you  
on  
for on  
gotta do  

\[Verse\]  
got done you for time you love for
go feeling s playing want fine stupid my i heart heart my playing you funny s my heart out you written lost a gets another on if on tell you can around on nobody t t t work me can can can knew can can, s on life me for
i i again care give swear i is, store cause pain be pain
ring had what my had your you you price style pay pay for for
i says to says an must im what good the before
, but same

\[Chorus\]  
from a left of dreams  
even though it seems  
to pretend as crazy i can see  
from a left of dreams  
even though it seems  
there s nothing left to me  

\[Bridge\]  
they t i boy that got know about
bout
baby out
better your love and so love your t called mind request the the be but the song the
i ya be dj beat the m joy man to
been way t always was you

## Evaluation ##

Chorus was the only section that had good results. The lines were surprisingly coherent. We didn't expect it to follow the repetitive format of pop choruses so well (1st and 2nd lines are the same as 4th and 5th lines) and were pleasantly surprised by this result. The rhyming matched the user input perfectly. At first glance, this chorus might even sound fluent. We rate this chorus Fluency: 3/5, Coherency: 4/5, Rhyming: 5/5, Topic: N/A.

The intro, verses, and bridge all had many repeating words as well as grammatical and spelling errors. Collectively, these scored Fluency: 0/5, Coherency 0/5, Rhyming: 5/5, Topic: N/A. The low scoring models for intro, verse, and bridge were mostly due to the fact that we had a lot less data to train those models compared to our chorus model. Plans to remedy this issue are outlined in the next section. 

Despite the poor quality of the sections besides chorus, we have a good framework to generate whole songs and we are confident that the other sections will catch up to the quality of the chorus. While our evaluation is biased since it is based off the opinions of three people working on this project, all of these generated lyrics have only reached a baseline of minimum fluency and coherency. When the quality improves, we can survey more people and gain direction towards tuning hyperparameters.

## Planned Improvements ##

To improve the quality of intro, verse, and bridge models, we plan on increasing the size of our datasets by downloading more song lyrics. We also plan on augmenting our datasets by  duplicating our current datasets to the end of themselves and shuffling. Some of the parameters we plan on iterating over are temperature (ie: "creativity" of the generations) and epochs (using different epochs for each of our different models). 

