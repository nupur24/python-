# -*- coding: utf-8 -*-
"""
Created on Fri May 18 13:46:19 2018

@author: HP
"""




import tweepy
 
# personal details
consumer_key ="bvA2daqZ601dQROcVHy5pB3xk"
consumer_secret ="2LoiRs4HmXZFGeZE6nY8wWt4b57Zx9zQPOIJwmcJcIU6VnxFWE"
access_token ="997356550707654657-t7y04cNnBZYU3Fteo0hET8b0UBHFWKf"
access_token_secret ="F3tiVVcX8p9PBLYn0a08DkXu5puctPUaQMzbDmjchlI8w"
 
# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
 
# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
 
# update the status
api.update_status(status ="Hello Everyone !")



