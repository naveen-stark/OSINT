import sys
try:
	import tweepy #https://github.com/tweepy/tweepy
except ImportError:
	print("You'll need tweepy instaled on your system.")
	sys.exit()
try:
	import csv
except ImportError:
	print("You'll need the python csv module installed on your system.")
	sys.exit()

consumer_key = "cLe4GmSwy8rhbiGYx0RUeCFqf"
consumer_secret = "G2qDNjUCove4psStRXIAjCfueIU7R7aKluVYL0aRyNfblp9LKu"
access_key = "1904711144-fN57cd5dWIEa50IgN2M7bhiiVH42p3hmR56USWJ"
access_secret = "no7D9Jxr9G0hwwP4KTtrxvmYYFOl6Px8ZG7SYQEQVH99p"


def get_all_tweets(screen_name):

	if (consumer_key == ""):
		print("You need to set up the script first. Edit it and add your keys.")
		return

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	

	alltweets = []	

	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	

	alltweets.extend(new_tweets)
	

	oldest = alltweets[-1].id - 1

	while len(new_tweets) > 0:
		print("getting tweets before %s" % (oldest))
		

		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		

		alltweets.extend(new_tweets)
		

		oldest = alltweets[-1].id - 1

		
		print("...%s tweets downloaded so far" % (len(alltweets)))
	

	outtweets = [[tweet.id_str, tweet.created_at, tweet.text] for tweet in alltweets]
	"""
	#write the csv	
	with open('%s_tweets.csv' % screen_name, 'w', encoding="utf-8") as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text"])
		writer.writerows(outtweets)
	"""
	return outtweets


if __name__ == '__main__':
	if (len(sys.argv) == 2):
		get_all_tweets(sys.argv[1])
	else:
	    print("Please add the twitter account you want to back up as an argument.")