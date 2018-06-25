# twitter-lists-bot

This telegram bot will keep you informed about new tweets from your twitter account list.
Just create a **public** list in your twitter account, add some members which you are interesting in,
 and the bot will resend their tweets to your telegram chat/group.

* Had been used [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot "python-telegram-bot API Library GitHub Repository") API Library, 
you can use *start_polling* or *webhook* updates methods to recieve the messages (see twitterlistsbot.py code and pyTelegramBotAPI Library manual)

* Had been used [Python API for Twitter](https://github.com/sixohsix/twitter "Python API for Twitter Library GitHub Repository") Library

### Install:

You need to install:

+ python (tested on 3.5+ version)
 
+ python-telegram-bot:

`$ sudo pip install python-telegram-bot --upgrade`

+ Python Twitter Tools

`$ sudo pip install twitter`

But in any case you must read authentic modules documentation to use it in your own operating system
 and environment.
 
 ### Settings:

Bot Settings are in the file **twitterlist/config.py:**

* put your *TG_BOT_TOKEN*
* id of chat or group where the bot will send messages *TG_YOUR_TELEGRAM_PRIVATE_CHAT_ID* (the bot should be an administrator there)
* your Twitter API application settings (you can create one here - https://apps.twitter.com/)
* your twitter account name *TW_LIST_OWNER_SCREEN_NAME*
* your **public** list name (slug) *TW_LIST_SLUG*
* a file name (with read/write permissions) to save list last read tweet ID - *TW_LAST_TWIT_ID_FILENAME*

The bot don't need your twitter account password and can't publish tweets from you or steal your personal information or something else, it uses only
 public information from your twitter account, that's why your twitter list could be public.
 
You can read some information about twitter list API if you are interesting in, here - https://developer.twitter.com/en/docs/accounts-and-users/create-manage-lists/api-reference 

### Run:

`$ python twitterlistsbot.py`

- you must use your python correct command depend of your python version and install path

### License

twitter-lists-bot is released under an MIT License.