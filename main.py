import tweepy
import discord
import requests
import os

CONSUMER_API_KEY = ''
CONSUMER_API_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''
BOT_TOKEN = ''

client = discord.Client()
auth = tweepy.OAuthHandler(CONSUMER_API_KEY, CONSUMER_API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
## api.update_status(status='hello')

@client.event
async def on_ready():
    print ("Logged in as " + client.user.name)
@client.event
async def on_message(message):
    ## print (message.channel)
    channel = str(message.channel)
    if (channel == 'success'):
        if (len(message.attachments) > 0):
            r = requests.get(message.attachments[0]['url'], stream=True)
            if r.status_code == 200:
                with open(message.id+'.png', 'wb') as f:
                    for chunk in r.iter_content(1024):
                        f.write(chunk)
                tweet(message.id+'.png', str(message.author))
def tweet (path, author):
    api.update_with_media(path, 'Success from ' + author)
    os.remove(path)
        
client.run(BOT_TOKEN)