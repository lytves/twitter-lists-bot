import os
import time

from twitterlist.config import TG_YOUR_TELEGRAM_PRIVATE_CHAT_ID, TW_LIST_OWNER_SCREEN_NAME, \
    TW_LIST_SLUG, TW_LAST_TWIT_ID_FILENAME
from twitterlist.utils import module_logger

TW_LAST_TWIT_ID_FULL_FILENAME = os.path.dirname(os.path.realpath(__file__)) + '/../' + TW_LAST_TWIT_ID_FILENAME


def check_twitter_api(bot, job):
    try:

        # to read a last twit ID from list
        with open(TW_LAST_TWIT_ID_FULL_FILENAME, 'rt') as file:

            last_twit_id = str(file.read())

            if last_twit_id is None:
                module_logger.error('Could not read from storage. Skipped iteration.')
                return

        module_logger.info('Last twit post ID = {!s}'.format(last_twit_id))

    except Exception as ex:

        module_logger.error('Exception of type {!s} in check_twitter_api(): {!s}'.format(type(ex).__name__, str(ex)))
        pass

    twitter = job.context
    response_obj = twitter.lists.statuses(owner_screen_name=TW_LIST_OWNER_SCREEN_NAME,
                               slug=TW_LIST_SLUG,
                               since_id=last_twit_id)

    # if exists new tweets in the list
    if (len(response_obj)) > 0:

        for twit in reversed(response_obj):

            mess_link = "https://twitter.com/" + twit['user']['screen_name'] \
                + "/status/" + twit['id_str']

            bot.send_message(chat_id=TG_YOUR_TELEGRAM_PRIVATE_CHAT_ID, text=mess_link)

            # write a new last tweet id
            try:
                with open(TW_LAST_TWIT_ID_FULL_FILENAME, 'wt') as file:

                    file.write(twit['id_str'])
                    module_logger.info('New last twit post ID is {!s}'.format((twit['id_str'])))

            except KeyError:

                module_logger.error(
                    'Exception of type {!s} in check_twitter_api(): {!s}'.format(type(ex).__name__, str(ex)))
                pass

            time.sleep(1)
