import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Output,Input,State
import plotly.graph_objs as go
from layout import html_layout

import datetime as dt
import pandas as pd



global yt_vid_comments
yt_vid_comments = []


from Youtube import search_vidid,all_cmt
from Senti import analyse_sentiment


from Reddit import top_posts
from Reddit import to_id_list
from Reddit import mine_comments



#Ye Wala sbb Change karna hai...

# query="Donald Trump"
days = dt.timedelta(days=10)
end_date = dt.date.today()
begin_date = end_date - days
# videoid_list=search_vidid(begin_date, end_date, query)

#ye wala aapna reddit ke liye hai
#ansdf=redditp(query)

# ansdf=all_cmt(videoid_list)
# ansdf = analyse_sentiment(ansdf,"comments")
# ansdf['Date'] = ansdf.apply(lambda row: str(row.CommentPublishDate).split("T", 1)[0], axis = 1)
# ansdf['RoundPolarity'] = round(ansdf['sentiment'],1)
#ansdf2 = ansdf.groupby('Date', as_index=False)[['sentiment']].sum()

#yaha tkk change karna hai





app = dash.Dash(__name__)
# app.layout = html.Div(
#     children=[
#         html.Div(
#             dcc.Input(
#                 id = "query-input",
#                 placeholder = "Search",
#                 type = "text",
#                 value = "Narendra Modi"
#         )
#     ),

#         html.Div(
#             dcc.Graph(
#                 id='line-graph',
#                 config={'displayModeBar': True},
#                 animate= True,
#                 figure=px.line(ansdf2,
#                                x='Date',
#                                y='sentiment',
#                                title='Line Graph analysis',
#                                ),
#                 style={'padding': 0, 'height':600}
#             )
#         ),

#         html.Div(
#             dcc.Graph(
#                 id='bar-graph',
#                 figure={
#                     'data': [
#                         {
#                             'x': ansdf['CommentPublishDate'],
#                             'y': ansdf['sentiment'],
#                             'name': 'Bar analysis',
#                             'type': 'bar'
#                         }
#                      ],
#                     'layout': {
#                             'title': 'Bar analysis.',
#                             'height': 600,
#                             'padding': 150
#                     }
#                 }),
#             ),

#         html.Div(
#             dcc.Graph(
#                 id='scatter-graph',
#                 config={'displayModeBar': True},
#                 animate= True,
#                 figure=px.scatter(ansdf,
#                                x='CommentPublishDate',
#                                y='sentiment',
#                                title='Scatter analysis',
#                                ),
#                 style={'padding': 25, 'height':600}
#             )
#         ),

#         html.Div(
#             dcc.Graph(
#                 id='pie-graph',
#                 config={'displayModeBar': True},
#                 animate= True,
#                 figure=px.pie(ansdf,
#                                values='sentiment',
#                                names='RoundPolarity',
#                                color_discrete_sequence=px.colors.sequential.RdBu,
#                                title='Pie analysis',
#                                ),
#                 style={'padding': 25, 'height':800}
#             )
#         ),

#         ],

#     id='dash-container',

# )


# data =  [trace_close]
# layout = dict(title="Youtube Sentiment Chart",
#               showLegend=False)

# fig = dict (data=data, layout=layout)

app.index_string = html_layout



tabs_styles = {
    'height': '44px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold'
}

tab_selected_style = {
    'borderTop': '3px solid blue',
    'padding': '6px',
    'fontWeight': 'bold'
}









app.layout = html.Div([
    dcc.Tabs([
        dcc.Tab(label='Home', value='tab-0', style=tab_style, selected_style=tab_selected_style, children=[
            html.P(""),
            html.H3("Welcome to SentiomentZION ")
        ]),
        dcc.Tab(label='YouTube', value='tab-1', style=tab_style, selected_style=tab_selected_style, children=[
            html.Div([
                #html.Div(html.H1(children="Team Zion")),
                html.P(""),
                html.H3("Enter the term you want to analyse"),
                html.Div([
                    dcc.Input(
                        id = "yquery-input",
                        placeholder = "Enter the query you want to search",
                        type = "text",
                        value = "Donald Trump"
                    ),

                   html.Button('Submit', id='ysubmit-val', n_clicks=0),
                ]),
                html.Div(
                    dcc.Graph(id="y-graph1",)
                    ),
                html.Div(
                    dcc.Graph(id="y-graph2",)
                    ),
                html.Div(
                    dcc.Graph(id="y-graph3",)
                    ),
                html.Div(
                    dcc.Graph(id="y-graph4",)
                    )

            ])
        ]),
        dcc.Tab(label='Twitter', value='tab-2', style=tab_style, selected_style=tab_selected_style, children=[
            html.Div([
                #html.Div(html.H1(children="Team Zion")),
                html.P(""),
                html.H3("Enter the term you want to analyse"),
                html.Div([
                    dcc.Input(
                        id = "tquery-input",
                        placeholder = "Enter the query you want to search",
                        type = "text",
                        value = "Donald Trump"
                    ),

                   html.Button('Submit', id='tsubmit-val', n_clicks=0),
                ]),
                html.Div(
                    dcc.Graph(id="t-graph1",)
                    ),
                html.Div(
                    dcc.Graph(id="t-graph2",)
                    ),
                html.Div(
                    dcc.Graph(id="t-graph3",)
                    ),
                html.Div(
                    dcc.Graph(id="t-graph4",)
                    )

            ])
        ]),
        dcc.Tab(label='Reddit', value='tab-3', style=tab_style, selected_style=tab_selected_style, children=[
            html.Div([
                #html.Div(html.H1(children="Team Zion")),
                html.P(""),
                html.H3("Enter the term you want to analyse"),
                html.Div([
                    dcc.Input(
                        id = "rquery-input",
                        placeholder = "Enter the query you want to search",
                        type = "text",
                        value = "Donald Trump"
                    ),

                   html.Button('Submit', id='rsubmit-val', n_clicks=0),
                ]),
                html.Div(
                    dcc.Graph(id="r-graph1",)
                    ),
                html.Div(
                    dcc.Graph(id="r-graph2",)
                    ),
                html.Div(
                    dcc.Graph(id="r-graph3",)
                    ),
                html.Div(
                    dcc.Graph(id="r-graph4",)
                    )

            ])
        ]),
    ])
])

@app.callback(Output("y-graph1","figure"),
    [Input('ysubmit-val', 'n_clicks')],
    [State("yquery-input","value")])
def update_fig(n_clicks,input_value):
    videoid_list=search_vidid(begin_date, end_date, input_value)
    ansdf=all_cmt(videoid_list)
    ansdf = analyse_sentiment(ansdf,"comments")
    ansdf['Date'] = ansdf.apply(lambda row: str(row.CommentPublishDate).split("T", 1)[0], axis = 1)
    ansdf['RoundPolarity'] = round(ansdf['sentiment'],1)

    data=[]
    trace_close = go.Scatter(x = list(ansdf.index),
                         y=list(ansdf.sentiment),
                         name="Close",
                         line=dict(color="#ff3333"))
    data.append(trace_close)
    layout = {"title": input_value }
    return{
        "data":data,
        "layout":layout
        }





if __name__ == "__main__":
    app.run_server(debug = True)
