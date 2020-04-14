### BLOG 3 ###  

<ins>**Project Proposal, Due April 14: Music Lyric Generation**</ins>  

**Minimal viable action plan with stretch goals:**  

<ins>Input:</ins> Song structure, topics and/or keywords for each part  
<ins>Output:</ins> Complete song with given structure and topics/keywords  
<ins>Technique:</ins> Deep learning using data from RhymeZone (or other rhyme database), and also from scraping lyrics using the Genius API  
<ins>Initial Goal:</ins> Generate a rnn model for generating one verse of a pop song from a topic, with rhymes built in  
<ins>Stretch Goal #1:</ins> Add song structure as an input so users can add a chorus and verses
<ins>Stretch Goal: #2</ins> Generate 6 rnn models for 3 music genres, allowing users to choose a combination of genres for their lyric generation  
<ins>Strecth Goal #3:</ins> Develop a front end for our application  

**Motivation:**  

To learn more about rnn's and NLP techniques.  Make rhymes with text generation instead of just training a model and running it.  We also have an interest in music and want to provide musicians an easy way to come up with lyrics and inspiration.  

**Related Work:**  

Tutorial for a similar project: [Article](https://towardsdatascience.com/how-to-build-and-deploy-a-lyrics-generation-model-framework-agnostic-589f3026fd53)  

Chinese poetry generation with planning based neural network: [Paper](https://arxiv.org/pdf/1610.09889.pdf)

Paper on poem generation where we are getting evaluation techniques: [Paper](https://www.aclweb.org/anthology/D14-1074.pdf)

Code using the Genius API and using a lyric dataset: [Rap Lyric Sentiment](https://github.com/Hugo-Nattagh/2017-Hip-Hop)


**Project Objectives:**  

We want to first have our project generate one verse of a pop song that rhymes from a user's topic.  

**Proposed Methodologies:**  

We are first going to use a Kaggle dataset to get the names of top songs based on their genres.  From these songs, we will scrape for their lyrics using the Genius API and build our dataset (the song lyrics will be separated by part - verse, chorus, bridge, etc.). We will have a dataset of rhyming words from CMU Pronunciation Dictionary. From these datasets we will create our RNN model, giving rhyming words a higher weight.

**Available Resources:**  

Kaggle has a dataset of songs based on genres.  CMU Pronunciation Dictionary has a dataset of words that rhyme with each other.  Genius has an API that gets you a specific song's lyrics.  We will probably use Google Cloud Compute to run our training and to make our models.

**Evaluation Plan:**  

We will evaluate our model in two ways.

First, we will do a quantitative evaluation by calculating the probability of generated songs. 

Second, we will do qualitative evaluation by surveying humans. We will first do a Turing test by inputting actual song names/topics into our model, then asking participants if they can tell the difference between the actual song lyrics vs. our generated lyrics. Then, we will have participants rate the computer generated output on three different dimensions: fluency, coherence, meaning, rhyme.

| Fluency   | Does the song read smoothly and fluently? |
| Coherence | Is the song coherent across lines?        |
| Meaning   | Does the song follow the given topic?     |
| Rhyme     | Does the song rhyme?                      |


