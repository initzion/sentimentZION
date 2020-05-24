import datetime as dt
import pandas as pd
from twitterscraper import query_tweets,query_user_info
from Senti import analyse_sentiment

#ipstr="covid-19"
def top_results(ipstr):
    two_months = dt.timedelta(days=60)
    end_date = dt.date.today()
    begin_date = end_date - two_months

    limit = 400
    lang = "english"

    tweets = query_tweets(ipstr, begindate=begin_date, enddate=end_date ,limit=limit, lang=lang)

    #df=pd.DataFrame(tweets,columns = ['screen_name','username','user id','tweet id','tweet url','timestamp','var','text','text html','links','hashtags','has media','img urls','video url','likes','retweets','replies','is replied','parent tweet id','reply to users'])
    df = pd.DataFrame(t.__dict__ for t in tweets)
    #df.sort_values(by=['likes','retweets','replies'], inplace=True, ascending=False)
    #removing unwanted columns
    df.drop(df.columns[[1,2,3,4,6,8,9,10,11,12,13,17,18,19,20]], axis = 1, inplace = True)
    #df = df[df.likes >=0]
    #df.set_index('username',inplace=True)
    #df.drop_duplicates(subset ="screen_name", inplace = True)
    return df



# def get_user_info(twitter_user):
#     """
#     An example of using the query_user_info method
#     :param twitter_user: the twitter user to capture user data
#     :return: twitter_user_data: returns a dictionary of twitter user data
#     """
#     user_info = query_user_info(user=twitter_user)
#     twitter_user_data = {}
#     twitter_user_data["user"] = user_info.user
#     twitter_user_data["location"] = user_info.location 
#     return twitter_user_data

# def get_user_info(screen_name):
#     c = twint.Config()
#     c.Username = screen_name
#     c.Pandas = True
#     c.User_full = True
#     twint.run.Lookup(c)
#     # loc = a.location
#     Users_df = twint.storage.panda.User_df
#     Users_df.drop_duplicates(subset ="name", keep = 'last', inplace = True)
#     return Users_df
#    return loc


# df = top_results("narendra modi")
# df = analyse_sentiment(df,"text")
# df['RoundPolarity'] = round(df['sentiment'],1)
# df['feel'] = ["Positive" if x >=0  "Negative"  if x >=0 else "Neutral"for x in df['sentiment']]
# ansdf3 = df.groupby('RoundPolarity', as_index=False)[['likes']].sum()
# df['Date'] = df.apply(lambda row: str(row.timestamp).split(" ", 1)[0], axis = 1)
# screen_name_list= df["screen_name"].tolist()
# for sname in screen_name_list:
#     get_user_info(sname)
# loc = get_user_info("Ajinkyashinde_")
