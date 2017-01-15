#!/usr/bin/python
import praw
import re
import random

# Quotes taken from: https://en.wikipedia.org/wiki/Allen_Carr
ac_quotes = \
[
" smokers do not receive a boost from smoking a cigarette: smoking only relieves the withdrawal symptoms from the previous cigarette, which in turn creates more withdrawal symptoms once it is finished. In this way the drug addiction perpetuates itself. ",
" The 'relief' smokers feel on lighting a cigarette, the feeling of being 'back to normal', is the feeling experienced by non-smokers all the time. So that smokers, when they light a cigarette are really trying to achieve a state that non-smokers enjoy their whole lives.",


]

reddit = praw.Reddit('acbot')

subreddit = reddit.subreddit("sandboxtest")

for comment in subreddit.stream.comments():
    print(comment.body)
    if re.search("cigarette", comment.body, re.IGNORECASE):
            ac_reply = "According to this british author of books about quitting smoking: " + random.choice(ac_quotes)
            comment.reply(ac_reply)
            print(all_reply)
