# Twitter Sentiment Analysis Project
#### Author: Eli Bolotin

### Project Description -

This is project seeks to answer the question:
* Are people that talk about fitness happier than people that talk about media (tv, movies, youtube, etc.)?
* Data source: Twitter data

### Viewing directions -

1. Read the project summary to learn about the project.
2. Review the Twitter_Sentiment_Analysis.pdf to review statistical analysis.
3. Open the TSA folder to review and understand the code. Start with the README.

### Directory contents -

* **Project_Summary.pdf** - summarizes the project
* **Twitter_Sentiment_Analysis.pdf** - Statistics analysis, round 1
	- Twitter_Sentiment_Analysis.Rmd - Rmd file
* **Twitter_Sentiment_Analysis_Exp_2.pdf** - Statistics analysis, round 2
	- Twitter_Sentiment_Analysis_Exp_2.Rmd - Rmd file
* **Samples_Round_1** - sample data, round 1
* **Samples_Round_2** - sample data, round 2

### Link to program -

[Twitter Sentiment Analyzer](https://github.com/ebolotin6/Twitter_Sentiment_Analyzer/ "Twitter Sentiment Analyzer") - This project is created entirely with this purpose-built program.

### Naming convention of sample data -

1. Say that created a stream of tweets for a group called "media". You gave your stream the name of 'streamed_tweets_media'. As a result, the stream file name would be:
	- 'streamed_tweets_media.json'

2. Then, clean this stream using the TSA program in the next section. The newly created file would have an "clean" appended to it. New file:
	- 'streamed_tweets_media_clean.csv'

3. Next, fetch non-filtered tweets for this stream. Three files are created:
	- 'streamed_tweets_clean_full.json' (this is the full data in json format)
	- 'streamed_tweets_clean_full_trunc.csv' (same data but limited columns for readability's sake)
	- 'streamed_tweets_clean_full_trunc.json' (same as the csv above but in json format)

4. Finally, create the sentiment analysis for the tweets. Output file:
	- 'streamed_tweets_media_clean_full_analysis.csv' (import this into R.)


Copyright 2018, All Rights Reserved.
