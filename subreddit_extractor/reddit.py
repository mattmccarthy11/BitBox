#!/usr/bin/env python2

# Import packages
from __future__ import print_function
import config
import praw
import os
import datetime
import pandas as pd

# Connect to reddit
red = praw.Reddit(user_agent='Subreddit Extraction of r/CryptoCurrency',
                     client_id=config.client, client_secret=config.secret,
                     username=config.user, password=config.password)

# Exploration
# Pandas DataFrame for subreddit
df = pd.DataFrame()
# Extract submission, comments, and metadata
subred = red.subreddit('CryptoCurrency')
subs = subred.hot(limit=None)
for sub in subs:
    # Submission information
    sub_info = {
        'Type' : 'Submission',
        'Title' : sub.title,
        'Body' : 'NULL',
        'Score' : sub.score,
        'Upvotes' : sub.ups,
        'Downvotes' : sub.downs,
        'Sub_URL' : sub.url,
        'Author' : sub.author
    }
#    sub_info = {}
#    sub_info['_TYPE'] = 'Submission'
#    sub_info['Title'] = sub.title
#    sub_info['Body'] = 'NULL'
#    sub_info['Score'] = sub.score
#    sub_info['Upvotes'] = sub.ups
#    sub_info['Downvotes'] = sub.downs
#    sub_info['Sub_URL'] = sub.url
#    sub_info['Author'] = sub.author
    df.append(sub_info, ignore_index=True)
    
    # Comments for each sub
    for cmt in sub.comments:
        # Comment information
        comment_info = {
            'Type' : 'Comment',
            'Title' : 'NULL',
            'Body' : cmt.body,
            'Score' : cmt.score,
            'Upvotes' : cmt.ups,
            'Downvotes' : cmt.downs,
            'Sub_URL' : 'NULL',
            'Author' : cmt.author
        }
#        comment_info = {}
#        comment_info['_TYPE'] = 'Comment'
#        comment_info['Title'] = 'NULL'
#        comment_info['Body'] = cmt.body
#        comment_info['Score'] = cmt.score
#        comment_info['Upvotes'] = cmt.ups
#        comment_info['Downvotes'] = cmt.downs
#        comment_info['Sub_URL'] = 'NULL'
#        comment_info['Author'] = cmt.author
        df.append(comment_info, ignore_index=True)

file_name = 'r/CryptoCurrency - ' + datetime.date.today().strftime('%Y%m%d') + '.csv'
df.to_csv(file_name)
