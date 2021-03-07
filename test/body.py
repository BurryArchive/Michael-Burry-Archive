import tweepy
import logging
import time
import random
from datetime import datetime, timedelta

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

from config import create_api
api = create_api()


def follow_a_person(api):
    while True:
        tweets = api.user_timeline(screen_name = "@michaeljburry", count =2)
        time.sleep(4*60)
        for tweet in tweets:
            time.sleep(5)
            try:
                tweet.favorite()
                api.update_status("@"+tweet.user.screen_name + "  @get_screenshot ", in_reply_to_status_id = tweet.id)
                print('tweeted')
                time.sleep(60)
            except Exception as e:
                print(e)
                break

while True:
    follow_a_person(api)
    time.sleep(10)
print('\n\n\n                   finished the process                           ')