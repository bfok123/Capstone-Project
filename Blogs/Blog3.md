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


**Project Objectives:**  

We want to first have our project generate one verse of a pop song that rhymes from a user's topic.  

**Proposed Methodologies:**  

We are first going to use a Kaggle dataset to get the names of songs based on their genres.  From these songs, we will scrape for their lyrics using the Genius API and build our dataset.  From this dataset we will create our rnn, giving rhyming words a higher weight.

**Available Resources:**  

Kaggle has a dataset of songs based on genres.  RhymeZone has a dataset of words that rhyme with each other.  Genius has an API that gets you a specific song's lyrics.  We will probably use google cloud compute to run our training and to make our models.

**Evaluation Plan:**  

This will be our hardest task since "how good" lyrics are is usually a matter of a person's opinion.


