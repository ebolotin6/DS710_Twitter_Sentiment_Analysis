# Eli Bolotin
# Twitter Sentiment Analysis Program
# Copyright 2018, All Rights Reserved.

from TwitterProgram import StreamedTweets, TweetProgram


# Step 1. Stream tweets for group 1 and 2 (Python step)
# 	- example: stream_tweets(workout_keyterms, option = 'user_info', file_name = 'streamed_tweets_workout', num_users = 2000)
# 	- Examine 'streamed_tweets_workout' to review 2000 tweets (manual step).
# 	- input: none
# 	- returns: json filename
# 	- creates: json file and csv file

# Open file: ProcessTweets.py

# Step 2. Clean the streamed tweets via program algorithm (Python step)
# 	- example: clean_tweets("streamed_tweets_workout.json")
# 	- Examine cleaned tweets and make changes if necessary.
# 	- input: json 
# 	- returns: csv file for streamed tweets
# 	- output: csv file for streamed tweets

# Step 3. Fetch other tweets in full data format for users in streamed groups of tweets (Python step). Store the full data, but present the user with a column-truncated version for readability.
# 	- example: get_full_tweets('streamed_tweets_workout.csv')
# 	- Examine the truncated tweets to review fetched tweets (manual step)
# 	- input: csv
# 	- returns: json
# 	- output: csv and json

# (OPTIONAL) Clean the fetched & truncated tweets via algorithm (Python step)
# 	- clean_tweets("streamed_tweets_workout_clean_truncated.json", tweets_type = "REST")
# 	- input: json
# 	- returns: json
# 	- output: csv and json

# Step 4. Generate sentiment for tweets
# 	- input: json
# 	- returns: csv
# 	- output: csv




######### Group 1 #########

### step 1 stream tweets
### step 2 instantiate object and clean tweets
group_1 = StreamedTweets("streamed_tweets_media.json", sub_dir="Samples_Round_2")
group_1.clean_tweets()

### step 3: fetch other tweets
group_1.get_full_tweets(max_users = 3000)

### step 4: clean the fetched tweets
group_1.clean_tweets(tweets_type = "full")

### step 5 - produce sentiment analysis of cleaned tweets. Remember, we are cleaning the full file, not the truncated version (which is the same as the full file, only less columns for readability).
group_1.get_sentiment()

######### Group 2 #########

### step 1 stream tweets
### step 2 instantiate object and clean tweets
group_2 = StreamedTweets("streamed_tweets_fitness.json", sub_dir="Samples_Round_2")
group_2.clean_tweets()

### step 3: fetch other tweets
group_2.get_full_tweets(max_users = 3000)

### step 4: clean the fetched tweets
group_2.clean_tweets(tweets_type = "full")

### step 5 - produce sentiment analysis of cleaned tweets. Remember, we are cleaning the full file, not the truncated version (which is the same as the full file, only less columns for readability).
group_2.get_sentiment()