### BLOG 3 ###  

<ins>**Project Proposal, Due April 14: Music Lyric Generation**</ins>  

**Minimal viable action plan with stretch goals:**  

<ins>Input:</ins> topics and/or keywords for each part  
<ins>Output:</ins> Rhyming verse that pertains to the given topics or keywords  
<ins>Technique:</ins> Deep learning using data from a popular song dataset from Kaggle and additional data using a script to scrape lyrics from Genius Lyrics. Scrape rhyming data from RhymeZone or download the CMU Pronunciation Dictionary.    
<ins>Initial Goal:</ins> Generate a RNN model for generating a rhyming verse of a pop song given a topic  
<ins>Stretch Goal #1:</ins> Add song structure as an input so users can add a chorus and verses  
<ins>Stretch Goal: #2</ins> Generate 6 RNN models for 3 music genres, allowing users to choose a combination of genres for their lyric generation  
<ins>Strecth Goal #3:</ins> Develop a front end for our application  

**Motivation:**  

We have an interest in music and want to provide music producers with an easy way to come up with lyrics and inspiration. Pop songs have a reputation of being formulaic, predictable, and sometimes nonsensical so we should be able to play off of these facts to generate passable lyrics. Despite this, many producers find that the melodic line is easy to come up with while lyrics are a pain point. We will provide the remedy to lyric writer's block.  

**Related Work:**  

Tutorial for a similar project: [Article](https://towardsdatascience.com/how-to-build-and-deploy-a-lyrics-generation-model-framework-agnostic-589f3026fd53)  
This article goes through the high level steps of building a text generation model with suggestions on how to incorporate song lyrics in the model.   

Chinese poetry generation with planning based neural network: [Paper](https://arxiv.org/pdf/1610.09889.pdf)  
For this poem generator, they gave users the ability to choose the poem structure in a planning phase, similar to our stretch goal to allow the user to choose song structure.

Paper on poem generation where we are getting evaluation techniques: [Paper](https://www.aclweb.org/anthology/D14-1074.pdf)

Code using the Genius API and using a lyric dataset: [Rap Lyric Sentiment](https://github.com/Hugo-Nattagh/2017-Hip-Hop)

Generating rhyming rap lyrics: [Generating rhymes with deep learning](https://swarbrickjones.wordpress.com/2016/11/07/deeprhyme-d-prime-generating-dope-rhymes-with-deep-learning/)  
An example of interesting and creative generated lyrics as well as failures. The failures in this project can help us decide what features will be too hard to implement and which features we can reach for to improve on existing projects.

**Project Objectives:**  

We want to first have our project generate one verse of a pop song that rhymes from a user's topic. We want the generated text to be creative, something that the user wouldn't have come up with but at the same time something that somebody could come up with. To be creative, it will not necessarily choose the highest probability sequence and we will forbid it from completely copying lines from the training set.   

Because creative text generation isn't novel, our main objective will be the rhyming aspect of lyric generation. At first we will focus on tail rhymes in couplets but we will explore internal rhymes and alliteration which is common in many song lyrics. Another novelty would be choice of genre. In particular, lyric generation based on pop music has not been done yet.  

**Proposed Methodologies:**  

We are first going to use a Kaggle dataset to get the names of top songs based on their genres.  From these songs, we will scrape for their lyrics using the Genius API and build our dataset (the song lyrics will be separated by part - verse, chorus, bridge, etc.). We will have a dataset of rhyming words from CMU Pronunciation Dictionary. From these datasets we will create our RNN model. We will first try to rhyme in couplets so for the last word in every other line we will force a rhyming word with the last word of the previous line.

**Available Resources:**  

Kaggle has a dataset of songs based on genres.  CMU Pronunciation Dictionary has a dataset of words that rhyme with each other.  Genius has an API that gets you a specific song's lyrics.  We will probably use Google Cloud Compute to run our training and to make our models.

**Evaluation Plan:**  

We will evaluate our model in two ways.

First, we will do a quantitative evaluation by calculating the probability of generated sequences. 

Second, we will do qualitative evaluation by surveying humans. We will first do a Turing test by inputting actual song names/topics into our model, then asking participants if they can tell the difference between the actual song lyrics vs. our generated lyrics. Then, we will have participants rate the computer generated output on three different dimensions: fluency, coherence, meaning, rhyme.

| Criterium | Explanation                               |
|-----------|-------------------------------------------|
| Fluency   | Does the song read smoothly and fluently? |
| Coherence | Is the song coherent across lines?        |
| Meaning   | Does the song follow the given topic?     |
| Rhyme     | Does the song rhyme?                      |


