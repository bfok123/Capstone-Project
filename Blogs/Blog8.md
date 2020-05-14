### BLOG 8 ###

**Due May 14:**  

Second advanced solution attempt. What did you try? Are there any exciting results? Any confusing results? What are the failure modes? What will you try next?

Summary

## New Dataset ##
We decided to switch our dataset to consist of songs retrieved from the Genius API.  We added 33 more pop artists to our list and acquired a total of 3120 songs (We removed all of the songs from the previous dataset that we got from Kaggle.

[Ranking](https://www.ranker.com/list/best-pop-artists-2019/ranker-music).

83928 Intros  
54373 Choruses  
3191 Verses  
15878 Bridge  
11684 Outros  

...

## Rhyming Engineering ##
This week we tried to do more strict post processing with the rhymes.  We did this by only selecting lines that rhymed with each other AND where the distance between each of them was 1 (meaning the were generated next to each other).  We predicted that this would help improve coherency between lines.

We could not tell which method worked better so we surveyed XXX amount of people.  These were the average results for coherency:

* No post processing:
* Original post processing:
* Strict post processing:
* Normal song:

From these results, we will be using ... from now on.

## Examples ##

\[Intro\]

hooked i on you you
fucked i went tired the understand tell do
ever people some i spreading to i
ladies i it my see my

\[Strict Rhyming Chorus\] 

oh know
cause i playing these games to stay
the one who s got time (oh
sunsets don t try to run away

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

\[Outro\]

worse can
and you
i until problem my in with goddamn
you you you

## Evaluation ##

## Planned Improvements ##
