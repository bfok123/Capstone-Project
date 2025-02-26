### BLOG 9 ###

**Due May 21:**   

Datasets for other genres, streamlined rhyming post-processing, attached to frontend, topic selection. We did not perform an evaluation this week because we didn't have any new models or algorithms that we needed to evaluate against each other. 

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
To start the application clone the repo, `pip install -r requirements.txt`, navigate to the frontend directory, and run index.py.  
Choose a genre, optionally define a topic, choose which sections to generate, choose the rhyming scheme of each section, and view the generated lyrics. Only pop and hip-hop work right now.
![app](https://github.com/bfok123/Capstone-Project/blob/master/images/frontend.png)

## Examples (Hip Hop) ##
[Intro]  
wherever team yeah  
excuse no! i yeah  
so shit  
i asked hoy it  

[Verse]  
and don't turn be young lie  
straight not into scream no new father nigga lie  
'spend all that night i'always on my body just a bag of this poppin'hard after all them bottom gave me a lil'bitch you know me i could feel the same that shit was goin'out everytime' on god you just can he get it go  
okay this verse is my bad from my name though where my lady'know told not know how would you would leave you do not like to i ask for   what i'm the best for me to she love you for that i' showing man that they can wish her just lie to lunch you build a bitch i'turn up her and put it though  

[Chorus]  
leave your sorrow on  
woo ooh take it to the head yeah drink it cause i don know about what you want from the money on  
like a thief in the night i take anything but some pussy she got that head like a dyke she got that head that i like deep in your partner right put that lil with make me a nigga that  
hey a bad uh nigga you know that i might be the trillest lil nigga that you know that i'm with none of these niggas in this that  

[Bridge]  
are good drunk i now i do i now i'''right right i right i got right i too could they so you never go they us know  
small town nigga hollywood dreams i know that everything'gold know  
back in 8th i  
celebrating i like i like the make sure luck remember i me i me i me i  

[Outro]  
by the dance'you with baby you with you with you me you with why like with back you with you bad hey sometimes i good that the i the i the i that i the i the you  
oh lord you can you  
love add'round that surely and eye surely we round we we'are''flip and add it see it cuddles see it  
i'crash get we get we get money the get we is get em addicted to the to the flip  

## Next Steps  ##
1. Train the rest of the models (all Minecraft models and Country Intro models)
2. Add more genres
3. Optimize post-processing algorithms. Right now it takes over a minute to generate an AABB section which means it can take over 5 minutes if a user wants to generate a whole song. We think there are a few places our post-processing algorithm can be optimized.
4. More post processing! (We got new bad output from our new models, so we want to try and fix these in our post processing)
