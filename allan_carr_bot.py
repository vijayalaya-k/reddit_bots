#!/usr/bin/python
import praw
import re
import random

# Quotes taken from: http://www.imdb.com/character/ch0007553/quotes
allan_quotes = \
[
" tbd ",
" tbd 2",


]

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("tbd")

for comment in subreddit.stream.comments():
    print(comment.body)
    if re.search("quit", comment.body, re.IGNORECASE):
            allan_reply = "Allan says: " + random.choice(allan_quotes)
            comment.reply(allan_reply)
            print(all_reply)
