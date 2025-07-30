import praw
import json

reddit = praw.Reddit(
    client_id="javOLiKf1MJV1v5UCk6R-A",       
    client_secret="f8esgxGkAKK4cwGyUgT2wzb1WvrSzQ", 
    user_agent="scraper_for_observation"
)

posts = []
for submission in reddit.subreddit("france").search("harcèlement", limit=100):
    posts.append({
        "title": submission.title,
        "text": submission.selftext,
        "author": str(submission.author)
    })

with open("reddit_posts.json", "w") as f:
    json.dump(posts, f, indent=2)

print(" Scraping terminé, 100 posts enregistrés dans reddit_posts.json")

