# Eli Bolotin
# Twitter Sentiment Analysis Program
# Copyright 2018, All Rights Reserved.

from TwitterProgram import MyStreamListener, stream_tweets

keywords_m1 = ['watching','watching show','greatest show','watch season','netflix','favorite show','best show','greatest movie','great acting','new season','watching tv','binge watching','newseries','binging','new episode','prime video','bestshowever','dvr','worst show','worst movie','love the movie','oscar worthy','movie sucks','atthemovies','film','horror','comedy','shortfilm']

keywords_m2 = ['#watchingshow','#greatestshow','#watchseason','#favoriteshow','#bestshow','#greatestmovie','#greatacting','#newseason','#watchingtv','#bingewatching','#newepisode','#primevideo','#worstshow','#worstmovie','#lovethemovie','#oscarworthy','#moviesucks']

keywords_f1 = ['health fitness','get fit','fitness','legday','workoutwednesday','treadmill','pilates','yoga','gym time','deadlift','squats','FitnessFriday','gymlife','workouts','fitness training','postgym','armday','shoulderday','fitnessgoals','runner','workout','workout motivation','lift hard','lift weight','go running','sweat forit','crossfit','morning workout','muscle','six pack','lunges','cardio','elliptical','cycling']

keywords_f2 = ['#health','#gymtime','#fitnesstraining','#workoutmotivation','#lifthard','#liftweight','#gorunning','#sweatforit','#morningworkout','#sixpack','#triathlon']

keywords_m = keywords_m1 + keywords_m2
keywords_f = keywords_f1 + keywords_f2

########################
#	 Execution   
########################

### step 1: media group
file_name_m = stream_tweets(keywords_m, option = 'user_info', file_name = 'streamed_tweets_media', max_tweets = 4000)

### step 1: athletic group
file_name_a = stream_tweets(keywords_f, option = 'user_info', file_name = 'streamed_tweets_fitness', max_tweets = 4000)