import os
from pprint import pprint
from dotenv import load_dotenv
from instagrapi import Client

load_dotenv()

# Access the variables
ACCOUNT_USERNAME = os.getenv("ACCOUNT_USERNAME")
ACCOUNT_PASS = os.getenv("ACCOUNT_PASS")

cl = Client()
cl.login(ACCOUNT_USERNAME, ACCOUNT_PASS)

user_id = cl.user_id_from_username(ACCOUNT_USERNAME)

followers_ids = set()
followers = cl.user_followers(cl.user_id)
for follower in followers:
    followers_ids.add(follower)

following_ids = set()
following = cl.user_following(cl.user_id)
for follower in following:
    following_ids.add(follower)

not_following_me_back = following_ids - followers_ids

for user_id in not_following_me_back:
    not_following_back_user = cl.username_from_user_id(user_id=user_id)
    print(not_following_back_user)
