# To mine the required data from Reddit

import praw
import pandas as pd

#REDDIT MAIN FUNCTION FOR MINING

reddit = praw.Reddit(client_id='client id', client_secret='client secret ', user_agent='Reddit WebScraping')


def top_posts(topic):
    posts=[]
    try:
        f_subreddit = reddit.subreddit(topic) 
        for post in f_subreddit.hot(limit=5):
            posts.append([post.title, post.score, post.id, post.num_comments])
        posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'num_comments'])
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
        return comments
    except:
        comments.append(["Null","0","0","Null","0","0"])
        comments=pd.DataFrame(comments,columns=['title','s_score','upvote_ratio','comments','c_score','c_date'])
        return comments

