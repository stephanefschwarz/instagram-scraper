from datetime import datetime
from itertools import dropwhile, takewhile
import argparse
import instaloader

def command_line_parsing():

    parser = argparse.ArgumentParser(description = __doc__)

    parser.add_argument('--username', '-user', 
                        dest='username', 
                        required=True,
                        help='Instagram account name',
                        default='ariellepedrosa')

    parser.add_argument('--date_since', '-since', 
                        dest='since', 
                        required=True,
                        default='2000-1-1',
                        help='Dataformat YEAR-MONTH-DAY')

    parser.add_argument('--date_until', '-until', 
                        dest='until', 
                        required=True,
                        default='2024-1-14',
                        help='Dataformat YEAR-MONTH-DAY')

    return parser.parse_args()

def main():
    
    args = command_line_parsing()

    username = args.username # "ariellepedrosa"
    SINCE = datetime(*[int(date) for date in args.since.split("-")]) # datetime(2000, 1, 1)
    UNTIL = datetime(*[int(date) for date in args.until.split("-")]) # datetime(2024, 1, 14)

    scraper = instaloader.Instaloader(download_videos=False, download_video_thumbnails=False)
    
    def download_users_posts_with_periods(username):
        posts = instaloader.Profile.from_username(scraper.context, username).get_posts()
        for post in takewhile(lambda p: p.date > SINCE, dropwhile(lambda p: p.date > UNTIL, posts)):
            scraper.download_post(post, username)
                
    download_users_posts_with_periods(username)
    


if __name__ == "__main__":
    
    main()