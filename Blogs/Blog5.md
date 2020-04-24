### BLOG 5 ###

**Due April 23:**  

Complete multiple strawman/baseline approaches, record their performance, plus perform error analysis.

For the following experiments we were able to clean the code to get rid of non-English lyrics and non-lyrical strings such as "[Chorus]" and "[Verse 1:]". The dataset was narrowed down to 34,798 pop songs from 1970 to 2016. A note that we forgot to mention in the previous blog post was that we only trained on 1,000 pop songs to save time. This time we were able to train on the whole dataset. 

**Baseline approach #2: Character-level**  
| Temperature | Generated Lyrics                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0.2         | I want to be the one that you want to be the one that you want to be the one that you are loved the silent with me the sun is the same time to see your heart the same time is all the way I can't fall in love with you And I can't stop the sun in the world You can see you and me and you can feel  I the world The sun is all the sunshine The sun is all the sun The sun is all the sun That you can see you and me and the sun is all the sun in the cold I can't stay it all the sun The shadow of your face But the sun is one of the sun The sun is all the morning and the past the sun |
| 0.5         |  f you want to say you can walk over the street But you like me in love with you And if you want to fall in love I need to stop me, yeah I wanna say it all the world I can see your heart of the day that you want The world of me to my heart I can't stop the cheating The sun will be the one that you co ou do I am here all my heart When I wanna see the side and the chances for the sun in the sing The bad is streets and what you want to be all the same day I know you can hear you hold on you I want you and me all you got the measure with the dreams of far away                 |


**Baseline approach #3: Word-level**  

