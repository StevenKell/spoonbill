
# coding: utf-8

# In[1]:

from textblob import TextBlob
import csv
import tweepy
import unidecode


# In[16]:

query_number = 0
query = ''
with open("auth.txt", "r") as authFile:
    authInfo = authFile.readlines()
auth1 = tweepy.auth.OAuthHandler(authInfo[0].replace("\n",""), authInfo[1].replace("\n",""))
auth1.set_access_token(authInfo[2].replace("\n",""), authInfo[3].replace("\n",""))
api1 = tweepy.API(auth1)

def search(query, query_number, api):
    print(api)
    print('Searching for Tweets related to ' + query)
    csvFile = open(query,'w')
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(["username","author id","created", "text", "retwc", "hashtag", "followers", "friends","polarity","subjectivity"])
    counter = 0

    for tweet in tweepy.Cursor(api.search, q = query, lang = "en", result_type = "popular", count = query_number).items():
        created = tweet.created_at
        text = tweet.text
        text = unidecode.unidecode(text) 
        retwc = tweet.retweet_count
        try:
            hashtag = tweet.entities[u'hashtags'][0][u'text'] #hashtags used
        except:
            hashtag = "None"
        username  = tweet.author.name            #author/user name
        authorid  = tweet.author.id              #author/user ID#
        followers = tweet.author.followers_count #number of author/user followers (inlink)
        friends = tweet.author.friends_count     #number of author/user friends (outlink)

        text_blob = TextBlob(text)
        polarity = text_blob.polarity
        subjectivity = text_blob.subjectivity
        csvWriter.writerow([username, authorid, created, text, retwc, hashtag, followers, friends, polarity, subjectivity])

        counter = counter + 1
        if (counter == query_number):
            break

    csvFile.close()

def mainMenu():
    options_d = ["1. Enter Twitter security keys", "2. Set number of Tweets to pull", "3. Set search query", "4. Begin search", "5. Exit"]
    
    selected_option = 0
    print ("Menu options")
    for line in options_d:
         print(line)
    while (selected_option == 0):
        selected_option = int(input('Please enter an option number '))
        if selected_option == 1:
            print("Not implemented")
            selected_option = 0
        elif selected_option == 2:
            query_number = int(input('Please enter the number of Tweets to pull. '))
            selected_option = 0
        elif selected_option == 3:
            query = input('Please enter a search term. ')
            selected_option = 0
        elif selected_option == 4:
            search(query, query_number, api1)
        else:
            print("Not a valid option number")
            selected_option = 0
mainMenu()


# 
