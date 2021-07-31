#!/usr/bin/env python
# coding: utf-8

# In[1]:


import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


# In[ ]:


###API ########################
ckey = "n56C4AKmG9Obcz9bzj5zKfbUK"
csecret = "O9uqQuv83e3fASIoS2lwJjI90UqKLSRypmZ0vU9krjxaXRjziP"
atoken = "2555475931-lJBrxC9wN5zLh2pppAgYh4f6aexBKMGppsrj5qS"
asecret = "2U5k6rSn2d7MVezZ5sBaR74emS2owbazncVtcERICxa73"
#####################################
class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print ("SAVED" + str(doc) +"=>" + str(data))
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
'''========couchdb'=========='''
server = couchdb.Server('http://cindyk:flutF74@localhost:5984/')  #('http://115.146.93.184:5984/')
try:
    db = server.create('juegos_olimpicos')
except:
    db = server['juegos_olimpicos']
    
'''===============LOCATIONS=============='''    
twitterStream.filter(locations=[-78.558004,-0.248771,-78.468045,-0.164851])  
#twitterStream.filter(track=['Tokyo2020'])


# In[ ]:




