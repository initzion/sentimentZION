
from twitterprocess import top_results
from Senti import analyse_sentiment
import plotly.graph_objs as go


#FUNCTION TO PLOT TWITTER GRAPHS
def TWT_graph(n_clicks,input_value):
    andf = top_results(input_value)
    andf = analyse_sentiment(andf,"text")
    andf['Date'] = andf.apply(lambda row: str(row.timestamp).split(" ", 1)[0], axis = 1)
    andf['RoundPolarity'] = round(andf['sentiment'],1)
    andf2 = andf.groupby('Date', as_index=False)[['sentiment']].sum()
    # ansdf3 = ansdf.groupby('RoundPolarity', as_index=False)[['Likes']].sum()

    data=[]
    trace_close = go.Scatter(x = list(andf2.Date),
                         y=list(andf2.sentiment),
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
    trace_close = go.Scatter(x = list(andf.timestamp),
                          y=list(andf.sentiment),
                          mode='markers',
                          name="markers",
                          marker_color=andf['sentiment'])
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
    trace_close = go.Box(x = list(andf.Date),
                         y=list(andf.sentiment),
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
    trace_close = go.Pie(labels=list(andf.roundoff),
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
