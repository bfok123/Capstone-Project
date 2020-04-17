### BLOG 4 ###

**Due April 16:**  

Complete at least one strawman/baseline approach, run experiments, and set up the evaluation framework.

**Strawman/baseline approach:**  
For our baseline approach we fed ~40,000 pop songs to a RNN. We did not tune any hyperparameters and we did not clean the data past getting rid of unicode characters that the parser could not read. Because of this, there are still some non-English song lyrics and other unclean texts.

**Running Experiments:**  
After running our experiments, we got some obvious pop inspired lines:

Still a new bad girl I don't see you  
Baby when you keep me  
Them mint hints love  
(I love you)  
Will it hurt  
(I'm gently in sex)  
Ever just watch me in you  

Clearly, these lyrics will score a 1 in every category of our evaluation but cleaning up the text, tuning hyperparameters, and training on higher quality text will make this very promising.

**Evalution Framework:** [Form](https://forms.gle/C3wxrpubr9reXXR37) This form will ask someone to rate two sets of song lyrics, actual lyrics and generated lyrics, on four criteria, fluency, coherency, following the given topic, and whether or not it rhymes. It will also ask if they can identify which song is the real/generated one. Fluency is how the lines sound and coherency is if all the lines make sense together (i.e. no contradictions).    
