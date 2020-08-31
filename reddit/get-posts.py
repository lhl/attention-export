#!/usr/bin/python3

import json
import os
from   pprint import pprint
import praw
import sys
import time

'''
Reddit API status page: https://reddit.statuspage.io/
Discussion: https://www.reddit.com/r/redditdev/
'''

creds = json.load(open('../_data/reddit.creds'))
client_id = creds['client_id']
client_secret = creds['client_secret']
refresh_token = creds['refresh_token']

# Connect - use auth.py to generate the refresh_token
# should not expire https://www.reddit.com/r/redditdev/comments/b6bu0j/refresh_token_expiration/
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     refresh_token=refresh_token,
                     user_agent='pensieve-import')
# print(reddit.auth.scopes())

def main():
  # print(reddit.auth.scopes())
  # listing = reddit.redditor('randomfoo2').comments.new()
  listing = reddit.user.me().submissions.new(limit=None)
  # listing = reddit.user.me().comments.hot(limit=None)
  # listing = reddit.user.me().comments.controversial(limit=None)

  for l in listing:
    # If file exists, break
    if os.path.exists('../_data/reddit/posts/{}.json'.format(l)):
      print('Skipping post {}...'.format(l))
      continue

    # https://praw.readthedocs.io/en/latest/code_overview/models/comment.html?highlight=comment#praw.models.Comment
    try:
      msg = {}
      submission = reddit.submission(id=l)

      msg['author_name'] = submission.author.name
      msg['created_utc'] = submission.created_utc
      msg['distinguished'] = submission.distinguished
      msg['edited'] = submission.edited
      msg['id'] = submission.id
      msg['is_self'] = submission.is_self
      try:
        msg['link_flair_text'] = submission.link_flair_text
        msg['link_flair_template_id'] = submission.link_flair_template_id
      except:
        pass
      msg['locked'] = submission.locked
      try:
        msg['name'] = submission.name
      except:
        pass
      msg['num_comments'] = submission.num_comments
      msg['over_18'] = submission.over_18
      msg['permalink'] = submission.permalink
      msg['score'] = submission.score
      msg['selftext'] = submission.selftext
      msg['spoiler'] = submission.spoiler
      msg['stickied'] = submission.stickied
      msg['subreddit_name'] = submission.subreddit.name
      msg['subreddit_id'] = submission.subreddit.id
      msg['subreddit_display_name'] = submission.subreddit.display_name
      msg['title'] = submission.title
      msg['upvote_ratio'] = submission.upvote_ratio
      msg['url'] = submission.url

      with open('../_data/reddit/posts/{}.json'.format(l), 'w') as msg_outfile:
        print('Writing post {}...'.format(l))
        json.dump(msg, msg_outfile)

      time.sleep(1)
    except:
      print('ERROR post {}...'.format(l))



if __name__ == "__main__":
  main()
