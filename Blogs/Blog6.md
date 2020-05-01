### BLOG 6 ###

**Due April 30:**  

First advanced solution attempt. What did you try? Are there any exciting results? Any confusing results? What are the failure modes? What will you try next?

For this week we devoted a lot of time to engineering rhyming post-generation. We also wanted to see how a smaller, more focused dataset affected the quality of lyrics. 

## New Dataset ##
Last week we saw that there were sections of our generation that looked a lot like choruses when we rearranged the lines to put rhymes closer together. We wanted to test if this could happen naturally so we trained a 2-layer, 128-cell LSTM for each section of each song. The sections were labeled in some of the songs and we got a total of  

Chorus (7893), Verse (1270), Bridge (618), Intro (136), Outro (118) on 4,132 songs.  

Although this was a big step down from our original 36,000 songs, we thought that the quality of labeled songs was closer to what we wanted for output so the results would be comparable to the full dataset. 

Like the previous week, we generated sequences with beam search and with temperatures around 0.7, 0.8, and 0.9. Temperature affects the randomness of what's chosen by the beam search. A lower temperature (0.5) would choose the highest probability word everytime like "yeah, yeah, yeah, ..., yeah" and a higher temperature (1.0) would sometimes choose low probabilty words outputting more "creative" lyrics. 

We mostly left temperature alone this week because we were focusing on getting good rhyming engineering.

## Rhyming Engineering ##
We approached rhyming a few different ways. We would first generate a long list of lyrics, about 100 lines, then group them into lines that all rhymed with each other. This was important to take advantage of attention, longer memory of previous generated words, to achieve coherency between lines. We would then use user input to order the rhymes. 

For example, user input: "AABB" would choose two couplets to output. From here, there were a few choices to supply those rhyming lines. Frequency, minimum distance between lines, average distance between lines, and choosing at random, all had merit when choosing pairs of rhyming lines. 
