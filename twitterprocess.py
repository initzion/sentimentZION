import datetime as dt
import pandas as pd
from twitterscraper import query_tweets,query_user_info
from Senti import analyse_sentiment

#TWITTER MAIN FUNCTION FOR MINING

def top_results(ipstr):
    two_months = dt.timedelta(days=60)
    end_date = dt.date.today()
    begin_date = end_date - two_months

    limit = 400
    lang = "english"

    tweets = query_tweets(ipstr, begindate=begin_date, enddate=end_date ,limit=limit, lang=lang)

    df = pd.DataFrame(t.__dict__ for t in tweets)

    df.drop(df.columns[[1,2,3,4,6,8,9,10,11,12,13,17,18,19,20]], axis = 1, inplace = True)

    return df

