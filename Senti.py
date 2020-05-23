from textblob import TextBlob


def analyse_sentiment(df , term):
    f_list=df[term].to_list()
    for l in f_list:
        if(l=="[removed]" or l=="[deleted]"):
            f_list.append(0)

    pol=list()
    for l in f_list:
        if(l!=0):
            analysis=TextBlob(l).sentiment
            t=analysis.polarity
            pol.append(t)
        else:
            pol.append(0)
        #print (pol)
    df['sentiment']=pol

    f_list=df["sentiment"].to_list()
    pol=list()
    for l in f_list:
        if(l>0):
            pol.append("Positive")
        elif(l<0):
            pol.append("Negative")
        else:
            pol.append("Neutral")
        #print (pol)
    df['roundoff']=pol

    df=df[df.sentiment != 0]
    return df
