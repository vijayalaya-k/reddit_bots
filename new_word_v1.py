#!/usr/bin/python
import praw
import json
import re
import random

# observe and collect words typed up. identify new words, validate if they are present in the dictionary json and provide meaning...

## read dictionay in Documents\Python\dictionary.json, read key and print value...



# crutch below.. remove when the code is complete.

   fruits = {
        'apple':1,
        'orange':2,
        'banana':3
    }

	#if key 'apple' exists in fruits?
    if 'apple' in fruits:
        print(fruits['apple'])


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
