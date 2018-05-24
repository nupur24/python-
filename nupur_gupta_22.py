


import oauth2 
import time 
import urllib2
import json


url1 = "https://api.twitter.com/1.1/search/tweets.json"  

params = {
        "oauth_version": "1.0",
        "oauth_nonce": oauth2.generate_nonce(),
        "oauth_timestamp": int(time.time())
    }

consumer = oauth2.Consumer(key="bvA2daqZ601dQROcVHy5pB3xk", secret="2LoiRs4HmXZFGeZE6nY8wWt4b57Zx9zQPOIJwmcJcIU6VnxFWE")

token = oauth2.Token(key="997356550707654657-t7y04cNnBZYU3Fteo0hET8b0UBHFWKf",
                     secret="F3tiVVcX8p9PBLYn0a08DkXu5puctPUaQMzbDmjchlI8w")

params["oauth_consumer_key"] = consumer.key   

params["oauth_token"] = token.key

params["q"] = "Jaipur"

req = oauth2.Request(method="GET", url=url1, parameters=params)
signature_method = oauth2.SignatureMethod_HMAC_SHA1() 
req.sign_request(signature_method, consumer, token)
url = req.to_url()
response = urllib2.Request(url)
data = json.load(urllib2.urlopen(response))



filename = params["q"]      
f = open(filename + "_File.txt", "w")  
json.dump(data["statuses"], f)
f.close()





























