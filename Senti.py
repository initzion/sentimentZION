from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from textblob import TextBlob


#ANALYSING SENTIMENT AND RATING THEM FROM -1 TO +1


def analyse_sentimentwt(df , term):
    authenticator = IAMAuthenticator('api-key')
    language_translator = LanguageTranslatorV3(
    version='date',
    authenticator=authenticator
    )

    language_translator.set_service_url('url')

    
    df[term].replace(['[deleted]','[removed]'],[1.1,1.1],inplace=True)

    f_list=df[term].to_list()

    for l in f_list:
        l=l.encode('unicode-escape').decode('utf-8')

        pol=list()
        for l in f_list:
            print(l,"\n")
            if (l!=1.1):
                language = language_translator.identify(l).get_result()
                n=language['languages']
                m=n[0]['language']
                if(m=='hi'):
                    translation = language_translator.translate(text=l,model_id='hi-en').get_result()
                    p=translation['translations']
                    k=p[0]['translation']
                    l=k
                    analysis=TextBlob(l).sentiment
                    t=analysis.polarity
                    pol.append(t)
                else:
                    pol.append(1.1)

    df['sentiment']=pol
    return df



def analyse_sentiment(df , term):
    f_list=df[term].to_list()
    pol=list()
    for l in f_list:
        analysis=TextBlob(l).sentiment
        t=analysis.polarity
        pol.append(t)
    df['sentiment']=pol
    pol2=list()
    for l in pol:
        if(l>0):
            pol2.append("Positive")
        elif(l<0):
            pol2.append("Negative")
        else:
            pol2.append("Neutral")
    df['roundoff']=pol2
    df=df[df.sentiment != 0]
    return df

def pretty_txt(input_value):
    input_value = input_value.replace(" ", "")
    input_value = input_value.replace("-", "")
    input_value = input_value.replace("[^a-zA-Z#]", " ")
    return (input_value)
