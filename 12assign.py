#ques1

#API Tokens is a bit of a general term.
#API token is a unique identifier of an application requesting access to your service.
#Your service would generate an API token for the application to use when requesting your service.
#API token is the form of authentication similar to a username/password.

Access_Token = "1009291346744508416-Q5fd5u1gTtAVyGcR9fBklAzvJZb9nk"

#ques2

#IP ADDRESS OF FACEBOOK IS = 103.54.100.205
#IP ADDRESS OF GOOGLE IS = 172.217.15.68

#ques3

from keys import Consumer_Key,Consumer_Secret,Access_Token,Access_Secret
import tweepy

oauth =tweepy.OAuthHandler(Consumer_Key,Consumer_Secret)
oauth.set_access_token(Access_Token,Access_Secret)
api=tweepy.API(oauth)
user= api.get_user('hitaishi')
print(api.search("#viratkohli"))

#ques4

#A library is a collection of functions / objects that serves one particular purpose. you could use a library in a variety of projects
#Library is written in same language which is a collection of all the functionalities required for the use case.
#Library: android.app.Activity library (Class with all code)

#An API is an interface for other programs to interact with your program or library  without having direct access.
#API is a part of library which defines how an application communicates with external code.
#API can be written in any language.
#API: Android API to interact with hardware, like the front camera of an Android-based device.

#ques5

from keys import consumer_key,consumer_secret,access_token,access_secret
import tweepy

oauth =tweepy.OAuthHandler(Consumer_Key,Consumer_Secret)
oauth.set_access_token(Access_Token,Access_Secret)
api=tweepy.API(oauth)
user= api.get_user('hitaishi')

#new function used!!!
api.update_status('tweepy + oauth!')











