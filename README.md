# rimshotbot
Discord bot that joins a Voice Channel and plays rimshots, "the price is right" riffs, and other nonsense.

This bot is written in Python and will require FFMpeg installed.


## Usage

In any text channel the bot has access to, you can send it commands.

Try %menu and it will give you a list of available sounds.

Some of the available sounds to play are:

* %rim - a typical comedy rimshot.
* %wrong - the "Price is Wrong" sound.
* %crickets - these insects, making their noises.
* %gong - a big messy sounding crash cymbal sound.

Join a Voice Channel to get these sounds going.  (If you don't the bot will warn you.)

Once the bot has joined a channel it will not join any other channel.  You'll have to kick it from the room.  :) 


## Setup

The same basic setup steps apply as in https://github.com/nthmost/discord-radio-bot 

Open up details.txt and copy in the details as you receive them from the Discord bot creation process.  Don't forget to do the last step in details.txt where you copy in the Client ID into the URL and then load that URL.  This step attaches your new bot to a target Discord Server.

Once you've done those, clone this repo and then:

* cd rimshotbot
* cp example.env .env
* vi .env

Fill in the TOKEN you got when you set up your bot.  Close and save the file.

Now set up a virtual environment (same as in discord-radio-bot instructions). 

After activating the virtual environment:

* pip install -r requirements.txt
* source .env
* python rimshotbot.py


If all has gone well, you should see the bot in your discord server.  Huzzah!




