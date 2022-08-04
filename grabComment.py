"""
it will receive a link and get the given text for the reddit comment
"""


#https://www.reddit.com/r/explainlikeimfive/comments/ue0par/eli5_what_did_edward_snowden_actually_reveal_abot/

import praw
from praw.models import MoreComments


# subreddit = reddit.subreddit("python")

# hot_python = subreddit.hot(limit=5)

# for submission in hot_python:
#     if not submission.stickied:
#         print(submission.title)


# submission = reddit.submission(url=url)

# print(dir(submission))
# print(submission.title)
# exit()
# for top_level_comment in submission.comments:
#     print(top_level_comment.body)


def createReddit():
    """
    Will create the reddit instance that will be used to grab the comments
    """
    with open('secrets.key') as f:
        lines = f.readlines()
        clientId = lines[1][:-1]
        client_secret = lines[0][:-1]
        username = lines[2]

    print(clientId, client_secret, username)

    reddit = praw.Reddit(client_id=clientId,
                     client_secret=client_secret, password='tiktokmaker2022',
                     user_agent='hazcoper', username=username)

    return reddit


def createSubmission(url, reddit):
    """
    Will receive a url and will grab the information from that url
    """

    return reddit.submission(url=url)

def grabTitle(submission):
    """
    Will grab the title from the submission
    """

    return submission.title

def grabMostLiked(submission):
    """
    Will return a list of the most liked comments
    it will be sorted by ups
    """
   
    allComments = []
    for top_level_comment in submission.comments:
        if isinstance(top_level_comment, MoreComments):
            continue
        allComments.append(top_level_comment)


    allComments = sorted(allComments, key=lambda x: x.ups, reverse=True)
    

    return allComments