# To mine the required data from Reddit

import praw
import pandas as pd

# from textblob import TextBlob
# import re


reddit = praw.Reddit(client_id='O819Gp7QK8_o5A', client_secret='4pC2Pu3eTJWxdSKfKscZYQOh2-o', user_agent='Reddit WebScraping')


def top_posts(topic):
    posts=[]
    try:
        f_subreddit = reddit.subreddit(topic) 
        for post in f_subreddit.hot(limit=5):
            posts.append([post.title, post.score, post.id, post.num_comments])
        posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'num_comments'])
        # posts.sort_values(by=['score','num_comments'], inplace=True, ascending=False)
        posts.set_index('title',inplace=True)
        return posts
    except:
        posts.append(["Null","0","0","0"])
        posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'num_comments'])
        return posts

def to_id_list(posts):
    id_list= posts["id"].tolist()
    return id_list


def mine_comments(id_list):
    comments=[]
    try:
        for i in id_list:
            submission = reddit.submission(id=i)
            submission.comments.replace_more(limit=None)
            for comment in submission.comments.list():
                comments.append([submission.title,submission.score,submission.upvote_ratio,comment.body,comment.score,comment.created_utc])
            comments=pd.DataFrame(comments,columns=['title','s_score','upvote_ratio','comments','c_score','c_date'])
            comments['c_date'] = pd.to_datetime(comments['c_date'],unit='s')
            # comments.sort_values(by=['c_date','s_score','c_score'], inplace=True, ascending=False)
            # comments.set_index('title',inplace=True)
        return comments
    except:
        comments.append(["Null","0","0","Null","0","0"])
        comments=pd.DataFrame(comments,columns=['title','s_score','upvote_ratio','comments','c_score','c_date'])
        return comments


# df1=top_posts("covid19")
# list1=to_id_list(df1)
# df=mine_comments(list1)
# df[df.comments != "[deleted]"]
# df[df.comments != "[removed]"]
# ansdf = analysereddit_sentiment(df,"comments")



# for l in f_list:
#      if(l=="[removed]" or l=="[deleted]"):
#          f_list.append(0)

# pol=list()
# for l in f_list:
#     if(l!=0):
#         re.sub(' +', ' ', l)
#         analysis=TextBlob(l).sentiment
#         t=analysis.polarity
#         pol.append(t)
#     else:
#         pol.append(0)
# df['sentiment']=pol
