
from Youtube import search_vidid,all_cmt
from Senti import analyse_sentiment
import plotly.graph_objs as go

import pandas as pd
import datetime as dt


#FUNCTION TO PLOT YOUTUBE GRAPH
days = dt.timedelta(days=10)
end_date = dt.date.today()
begin_date = end_date - days

global yt_vid_comments
yt_vid_comments = []

def YT_graph(n_clicks,input_value):
    videoid_list=search_vidid(begin_date, end_date, input_value)
    ansdf=all_cmt(videoid_list)
    ansdf = analyse_sentiment(ansdf,"comments")
    #answt = analyse_sentimentwt(ansdf,"comments")
    ansdf['Date'] = ansdf.apply(lambda row: str(row.CommentPublishDate).split("T", 1)[0], axis = 1)
    ansdf['RoundPolarity'] = round(ansdf['sentiment'],1)
    ansdf2 = ansdf.groupby('Date', as_index=False)[['sentiment']].sum()
    #yaha tkk toh bss dataframe creation hai jo tere paas hai
    data=[]
    trace_close = go.Scatter(x = list(ansdf2.Date),
                         y=list(ansdf2.sentiment),

                         name="Close"
                         )
    data.append(trace_close)
    figure1 = go.Figure(data)
    figure1.update_layout(
    title="Date-Wise Cumulative Sentiment Score Line Plot",
    xaxis_title="Date",
    yaxis_title="Cumulative Score",
    template='plotly_dark',
    plot_bgcolor= 'rgba(0, 0, 0, 0)'
    )

    data=[]
    trace_close = go.Scatter(x = list(ansdf.CommentPublishDate),
                         y=list(ansdf.sentiment),
                         mode='markers',
                         name='markers',
                         marker_color=ansdf['sentiment']
                         )

    data.append(trace_close)
    figure2 = go.Figure(data)
    figure2.update_layout(
    title="Date-Wise Sentiment Score Scatter Plot [negative(-1) to positive(+1)]",
    xaxis_title="Date",
    yaxis_title="(-ve) Sentiment Score (+ve)",
    template='plotly_dark',
    plot_bgcolor= 'rgba(0, 0, 0, 0)'
    )

    data=[]
    trace_close = go.Box(x = list(ansdf.Date),
                         y=list(ansdf.sentiment),
                         name="Close",
                         line=dict(color="#ff3333"))
    data.append(trace_close)
    figure3 = go.Figure(data)
    figure3.update_layout(
    title="Date-Wise Sentiment Score Box Plot [negative(-1) to positive(+1)]",
    xaxis_title="Date",
    yaxis_title="(-ve) Sentiment Score (+ve)",
    template='plotly_dark',
    plot_bgcolor= 'rgba(0, 0, 0, 0)'
    )

    data=[]
    trace_close = go.Pie(labels=list(ansdf.roundoff),
                         name="Close"
                         )
    data.append(trace_close)
    figure4 = go.Figure(data)
    figure4.update_layout(
    title="Pie-Chart",
    template='plotly_dark',
    plot_bgcolor= 'rgba(0, 0, 0, 0)'
    )
    figure = (figure1,figure2,figure3,figure4)

    return figure
