from Reddit import top_posts
from Reddit import to_id_list
from Reddit import mine_comments

import plotly.graph_objs as go

from Senti import analyse_sentiment,pretty_txt
#FUNCTION TO PLOT REDDIT GRAPH


def REDDIT_graph(n_clicks,input_value):
    input_value = pretty_txt(input_value)
    df1=top_posts(input_value)
    list1=to_id_list(df1)
    comment=mine_comments(list1)
    comment=analyse_sentiment(comment,"comments")
    comment['Date'] = comment.apply(lambda row: str(row.c_date).split(" ", 1)[0], axis = 1)
    comment2 = comment.groupby('Date', as_index=False)[['sentiment']].sum()
    data=[]
    trace_close = go.Scatter(x = list(comment2.Date),
                         y=list(comment2.sentiment),
                         mode='lines',
                         name="Close",
                         line=dict(color="#ff3333"))
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
    trace_close = go.Scatter(x = list(comment.c_date),
                          y=list(comment.sentiment),
                          mode='markers',
                          name="markers",
                          marker_color=comment['sentiment'])
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
    trace_close = go.Box(x = list(comment.Date),
                         y=list(comment.sentiment),
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
    trace_close = go.Pie(labels=list(comment.roundoff),
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
