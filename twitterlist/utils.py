# start logging to the file with log rotation at midnight of each day
import os
import logging

from logging.handlers import TimedRotatingFileHandler

formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
handler = TimedRotatingFileHandler(os.path.dirname(os.path.realpath(__file__)) + '/../twitterlistbot.log',
                                   when='midnight',
                                   backupCount=10)
handler.setFormatter(formatter)
module_logger = logging.getLogger(__name__)
module_logger.addHandler(handler)
module_logger.setLevel(logging.INFO)
# end of log section
