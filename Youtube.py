from apiclient.discovery import build
from rfc3339 import rfc3339
import pandas as pd


global yt_vid_comments
yt_vid_comments = []

#YOUTUBE MAIN FUNCTION FOR MINING



DEVELOPER_KEY = "Api-key"

YOUTUBE_API_SERVICE_NAME = "youtube"

YOUTUBE_API_VERSION = "v3"


youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,  developerKey = DEVELOPER_KEY)
def search_vidid(startdate,enddate,query):


    publishedBefore = enddate
    publishedAfter = startdate

    publishedBefore = rfc3339(publishedBefore)
    publishedAfter = rfc3339(publishedAfter)

    query = query + " english news"
    req=youtube.search().list(q=query,part='snippet',type='video',publishedAfter = publishedAfter,publishedBefore = publishedBefore,maxResults=10)
    res = req.execute()
    videoid_list=[]
    for item in res['items']:
        videoid_list.append(item['id']['videoId'])
    return videoid_list

def ct_yt(vid):
    comlist=[]
    request = youtube.commentThreads().list(
       part="snippet",
       maxResults=100,
       order="relevance",
       textFormat="plainText",
       videoId=vid
   )
    resp = request.execute()
    for x in resp['items']:
        A=[x['snippet']['topLevelComment']['snippet']['textDisplay'],x['snippet']['topLevelComment']['snippet']['likeCount'],x['snippet']['topLevelComment']['snippet']['publishedAt'],x['snippet']['topLevelComment']['snippet']['updatedAt']]
        comlist.append(A)
    yt_vid_comments.extend(comlist)
    #return comlist

def all_cmt(videoid_list):
    for id in videoid_list:
        try:
            ct_yt(id)
        except:
            continue
    ansdf=pd.DataFrame(yt_vid_comments,columns = ['comments','LikeCount','CommentPublishDate','CommentUpdateDate'])
    return ansdf
