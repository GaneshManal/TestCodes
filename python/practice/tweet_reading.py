import tweepy
import json
import requests

# consumer_key = 'eDpwuOF0vafv0M2HIuD0bTnqy'
consumer_key = 'vea8UWSZ77owFqqfKJpn1acyg'

# consumer_secret = 'JAJxnmcEUkdBNq5oIiBTs8dw5VU9vzMNci4Ds2DnI16fGXF2Lk'
consumer_secret = 'Yq0qyY7nLrNEoZZDuivxHP3ArlodRrsC6wVNrHFzVOfurtipRe'

access_token ='138326156-0xKBUMzt0rYtaGHPP3fkyJJ1Klby91t0cdFoyJLZ'
access_token_secret = '2fYfWuGKcAsSxqhuFpa3joGg1JGhMKmtH1hP2gjmft65j'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
# print(dir(api))

'''
public_tweets = api.home_timeline()
for (idx, tweet) in enumerate(public_tweets[0:2]): #First 3 tweets in my public feed
    print('TWEET %s:\n\n\t%s\n\n' % (idx, tweet.text))
'''

'''
followers = api.followers()
for item in followers:
    print('---->', item)
'''

# top10 = api.trends_place(id=2473224)
# print(json.dumps(top10))

response = requests.get('https://api.twitter.com/1.1/trends/available.json')
print(response)

