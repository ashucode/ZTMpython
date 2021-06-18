import tweepy,sys,time


with open('tweet_keys.txt','r') as file:
	key_fie=file.read()

auth_data=key_fie.split('\n')
for i in auth_data:
	if i.split(':')[0]=='API key':
		api_key=i.split(':')[1]
	elif i.split(':')[0]=='API secret key':
		api_secret_key=i.split(':')[1]
	elif i.split(':')[0]=='Access Token':
		access_token=i.split(':')[1]
	elif i.split(':')[0]=='Access Token Secret':
		access_token_secret=i.split(':')[1]


auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)
user=api.me()
public_tweets = api.home_timeline()



for tweet in public_tweets:
    #print(tweet.text)
    pass

my_followers=[]
my_friends=[]
for follower in (tweepy.Cursor(api.followers).items()):
	my_followers.append(follower)

for friend in tweepy.Cursor(api.friends).items():
	my_friends.append(friend)

for follower in my_followers:
	if follower not in my_friends:
		follower.follow()
		print('followed Mr. ',follower.name)


search_string= 'india'
num_searches=2

for tweet in tweepy.Cursor(api.search,search_string).items(num_searches):
	try:
		tweet.favorite()
		tweet.retweet()
		print(tweet.text)
	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
		break
