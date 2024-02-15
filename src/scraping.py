from datetime import datetime
from itertools import dropwhile, takewhile
import csv
import instaloader


l = instaloader.Instaloader(download_videos=False, download_video_thumbnails=False)
username = "ariellepedrosa"

def download_users_posts_with_periods(username):
    posts = instaloader.Profile.from_username(l.context, username).get_posts()
    SINCE = datetime(2000, 1, 1)
    UNTIL = datetime(2024, 1, 14)
    for post in takewhile(lambda p: p.date > SINCE, dropwhile(lambda p: p.date > UNTIL, posts)):
        l.download_post(post, username)
            
download_users_posts_with_periods(username)
