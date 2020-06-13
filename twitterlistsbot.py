from telegram.ext import Updater
from twitter import *

from twitterlist.config import TG_BOT_TOKEN,\
    TW_ACCESS_TOKEN, TW_TOKEN_SECRET, TW_CONSUMER_KEY, TW_CONSUMER_SECRET
from twitterlist.handlers import *
from twitterlist.utils import module_logger


def main():

    # to create Twitter API object
    twitter = Twitter(
        auth=OAuth(TW_ACCESS_TOKEN, TW_TOKEN_SECRET, TW_CONSUMER_KEY, TW_CONSUMER_SECRET))

    module_logger.info("Start the twitter-lists-bot bot!")

    # create an object "bot"
    updater = Updater(token=TG_BOT_TOKEN, use_context=True)

    # here put the jobs for the bot
    job_queue = updater.job_queue

    # check twitter list - each 60sec, start on 5sec after the bot starts
    job_queue.run_repeating(check_twitter_api, 60, 5, context=twitter)

    # Start the Bot start_polling() method
    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.start_polling()
    updater.idle()

    # Start the Bot set_webhook() method
    # put your server IP adress instead 0.0.0.0
    # and see this page https://github.com/python-telegram-bot/python-telegram-bot/wiki/Webhooks
    # updater.start_webhook(listen='127.0.0.1', port=5007, url_path=TG_BOT_TOKEN)
    # updater.bot.set_webhook(url='https://0.0.0.0/' + TG_BOT_TOKEN,
    #                  certificate=open('/etc/nginx/PUBLIC.pem', 'rb'))


if __name__ == '__main__':
    main()
