### BLOG 9 ###

**Due May 21:**   

Datasets for other genres, streamlined rhyming post-processing, attached to frontend, topic support.

## New Datasets ##
We were happy with our pop dataset that we created by scraping Genius Lyrics last week so this week we gathered datasets for other genres, hip-hop, country, and Minecraft, like we planned in our project proposal. We scraped 40 songs from each of the 30 top artists of each genre in 2019 except for Minecraft which we could only find 6 high-profile artists on Genius Lyrics. Like the pop dataset, we split each of the other datasets into intros, verses, choruses, bridges, and outros. We only had time to train the models for hip-hop this week.
Breakdown of datasets:
| Pop                                                                     | Hip-hop                                                                | Country                                                               | Minecraft                                                         |
|-------------------------------------------------------------------------|------------------------------------------------------------------------|-----------------------------------------------------------------------|-------------------------------------------------------------------|
| Chorus 72631<br>Verse 52277<br>Intro 2955<br>Outro 7414<br>Bridge 10661 | Chorus 23804<br>Verse 41787<br>Intro 3383<br>Outro 2808<br>Bridge 1979 | Chorus 20798<br>Verse 12088<br>Intro 207<br>Outro 1835<br>Bridge 2413 | Chorus 1947<br>Verse 2014<br>Intro 157<br>Outro 150<br>Bridge 296 |

## Post-processing ##
This week, we worked a lot on editting out lines after they were generated.  Here is a list of things we tackled this week
* Removed repeated words
* Used Regex to remove stray characters caused by our model's inability to deal with puncuation
* Added apostrophes for words like don't and can't
* Improved the efficiency of our rhyming algorithm in mulitple ways (ie: only generating as many lines as needed for the given rhyming scheme)
* Removed the strict rhyming algorithm due inconsistency and processing time (Some generations took up to 10 minutes depending on the rhyming scheme)

Overall these improvements have removed almost all of the gibberish generated from our model, and can generate four lines of rhyming lyrics for most models in under a minute.

## Frontend ##
To start the application clone the repo, navigate to the frontend directory, and run index.py.  
Choose a genre, optionally define a topic, choose which sections to generate, choose the rhyming scheme of each section, and view the generated lyrics. Only pop and hip-hop work right now.
![app](https://github.com/bfok123/Capstone-Project/blob/master/images/frontend.png)

## Examples ##

### No Rhyming ###


## Next Steps  ##
1. Train the rest of the models (all Minecraft models and Country Intro models)
2. Add more genres
3. Optimize post-processing algorithms. Right now it takes over a minute to generate an AABB section which means it can take over 5 minutes if a user wants to generate a whole song. We think there are a few places our post-processing algorithm can be optimized.
