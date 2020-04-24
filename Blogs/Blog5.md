### BLOG 5 ###

**Due April 23:**  

Complete multiple strawman/baseline approaches, record their performance, plus perform error analysis.

For the following experiments we were able to clean the code to get rid of non-English lyrics and non-lyrical strings such as "[Chorus]" and "[Verse 1:]". The dataset was narrowed down to 34,798 pop songs from 1970 to 2016. A note that we forgot to mention in the previous blog post was that we only trained on 1,000 pop songs to save time. This time we were able to train on the whole dataset. 

**Baseline approach #2: Character-level**  

Loss = 1.4292  
| Temperature | Generated Lyrics                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0.2         | I want to be the one that you want<br>to be the one that you want<br>to be the one that you are<br>loved the silent with me<br>the sun is the same time to see your heart<br>the same time is all the way<br>I can't fall in love with you<br>And I can't stop the sun in the world<br>You can see you and me and you can feel<br><br>I the world<br>The sun is all the sunshine<br>The sun is all the sun<br>The sun is all the sun<br>That you can see you and me and the sun is all the sun in the cold<br>I can't stay it all the sun<br>The shadow of your face<br>But the sun is one of the sun<br>The sun is all the morning and the past the sun |
| 0.5         | <br>f you want to say you can walk over the street<br>But you like me in love with you<br>And if you want to fall in love<br>I need to stop me, yeah<br>I wanna say it all the world<br>I can see your heart of the day that you want<br>The world of me to my heart<br>I can't stop the cheating<br>The sun will be the one that you co<br>ou do<br>I am here all my heart<br>When I wanna see the side and the chances for the sun in the sing<br>The bad is streets and what you want to be all the same day<br>I know you can hear you hold on you<br>I want you and me all you got the measure with the dreams of far away                          |

We saw a few problems with a character-level model. It took almost twice as long to run compared to word-level (8 hours per epoch) and there would be weird cases where there wouldn't be full words. For these reasons, we chose to stick with word-level models for the rest of the project.  

**Baseline approach #3: Word-level**  

Loss = 3.5405  
For our word-level model, we found that a temperature below 0.9 did not output anything and a temperature in the range of 0.9 to 1.1 output the best results qualitatively. We didn't figure out how to incorporate rhymes into the model yet, so we generated a very long list of lines and reordered the lines so all the rhyming lines were next to each other. Since all lines were generated on the same call to the model, the lines were fairly coherent.

> a plastic smile for my hands of love<br>i be the one to blame, he's the one

> when you're into the air<br>when you're out there<br>don't end all of your tears<br>but i'm holding out there

> you find me completely let i know you ma<br>well still here for ya<br>crazy nights (if you don't me) i'm (baby i don't stop)<br>you find me completely let i know you ma<br>well still here for ya<br>but the music's all i gotta do or die i'm not<br>black diamond diamond rings ring the alarm<br>you find me completely let i know you ma<br>well still here for ya

The last set of lyrics makes a pretty good chorus.  
However, the results are not good enough to use the evaluation survey we made last week. It's pretty clear fluency and coherency did not improve enough to trick a human. We are not able to generate text with a given topic yet. We implemented rhyming with a brute force approach so we won't be happy with that until we can engineer it into a more realistic format. We wrote an evaluator for rhyming that outputs the percentage of rhymes in the generated song so we can check if the engineering is working. For the above examples, the generated song was 75.98% rhymes. 

For next week we will train for more epochs, use higher dimensional word embeddings, allow a larger vocabulary, experiment with dropout, and find a better way to implement rhyming. We plan to improve our evaluation framework by performing a grammar check for fluency. There is still some data cleaning that we have to do such as getting rid of "chorus" and "verse" and "\n"'s that appear the wrong places. We will also plan to extract a smaller but cleaner dataset and augment the original dataset with copies of the clean set. 
