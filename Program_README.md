# Twitter Sentiment Analysis (TSA) Program
### Eli (Ilya) Bolotin
---

### Program Description -

1. This program is designed to collect, clean and produce sentiment analysis for a statistics experiment using Twitter data.
2. The TSA program consists of 3 files:
	* TwitterProgram.py - core program
	* StreamTweets.py - executes step 1 
	* ProcessTweets.py - executes steps 2, 3, 4
3. Output: sentiment analysis

### Experiment Description -

The original question that this program was designed to answer was:
* Are people that talk about fitness happier than people that talk about media (tv, movies, youtube, etc.)?
* This is an experiment in which we are comparing 2 different groups (samples).

### Experiment workflow -

Consider 2 groups (example): people that talk (tweet) about fitness and people that tweet about media.
1. Create (unbiased) keywords and hashtags that define these groups.
2. Stream tweets using keywords/hashtags for both groups (Twitter Stream API)
3. Clean the streamed tweets (via program)
4. Fetch other (non-filtered) tweets for users in streamed groups.
5. Run sentiment analysis for fetched tweets.
6. Conduct statistical analysis in R.

### Directions for program execution (program workflow) -

* Step 1: Open StreamTweets.py and define keywords/hashtags for 2 groups
* Step 2: Run StreamTweets.py to collect streamed tweets.
	- Once streams have completely downloaded, proceed to step 2.
* Step 3: Run ProcessTweets.py to clean, fetch, and analyze sentiment for tweets.
* Step 4: Conduct analysis in R.

#### Further documentation found in the files above.

#### Copyright 2018, All Rights Reserved.