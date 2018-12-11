# Twitter Sentiment Analysis Project
#### Author: Eli Bolotin

### Project Description -

This is project seeks to answer the question:
* Are people that talk about fitness happier than people that talk about media (tv, movies, youtube, etc.)?
* Data source: Twitter data

### Viewing instructions -

1. Read the **Project_Summary.pdf** to learn about the project.
2. Review the **Twitter_Sentiment_Analysis.pdf** to understand statistical analysis.
3. Check out [**Twitter_Sentiment_Analyzer**](https://github.com/ebolotin6/Twitter_Sentiment_Analyzer) to review project code.

### Project (directory) contents -

* **Project_Summary.pdf** - summarizes the project
* **Twitter_Sentiment_Analysis.pdf** - Statistics analysis (sample set 1)
	- Twitter_Sentiment_Analysis.Rmd - R Markdown
* **Twitter_Sentiment_Analysis_Exp_2.pdf** - Statistics analysis, (sample set 2)
	- Twitter_Sentiment_Analysis_Exp_2.Rmd - R Markdown
* **/Samples_Round_1/** - sample data (set 1)
* **/Samples_Round_2/** - sample data (set 2)

### Link to program -

[Twitter Sentiment Analyzer](https://github.com/ebolotin6/Twitter_Sentiment_Analyzer/ "Twitter Sentiment Analyzer") - This project is created with this program.

### Naming convention of sample data -

1. Say that you created a stream of tweets for a group called "media". You gave your stream the name of '*streamed_tweets_media*'. As a result, the stream file name would be:
	- '*streamed_tweets_media.**json***'

2. Then, clean this stream using the [TSA Program](https://github.com/ebolotin6/Twitter_Sentiment_Analyzer/ "Twitter Sentiment Analyzer"). The newly created file would have "clean" appended to it:
	- '*streamed_tweets_media_clean.**csv***'

3. Next, fetch non-filtered tweets for the cleaned stream. Three files are created:
	- '*streamed_tweets_clean_full.**json***' (this is the full data in json format)
	- '*streamed_tweets_clean_full_trunc.**csv***' (full data with limited columns for readability)
	- '*streamed_tweets_clean_full_trunc.**json***' (same as the csv above but in json format)

4. Finally, create the sentiment analysis for the tweets. Output file:
	- '*streamed_tweets_media_clean_full_analysis.**csv***' (import this into R.)

<br /><br />
Copyright 2018 Eli Bolotin, All Rights Reserved.
