
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_auth
import plotly.plotly as py
import plotly.graph_objs as go

VALID_USERNAME_PASSWORD_PAIRS = [
    ['hello', 'dasha']
]

app = dash.Dash()
colors = {
    'background': '#ffffff',
    'text': '#B22222'
}

auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)


app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Ukrainian gross domestic product (GDP)',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div(children='Current US$', style={
        'textAlign': 'center',
        'color': colors['text'], 'fontSize': 25
    }),
    html.Div([html.Div([html.H3('Major Sectors', style = {'textAlign': 'center', 'color': '#ff794d'}),dcc.Graph(
        id='Graph1',
        figure={
            "data": [
                {
                    "values": [12, 28, 59],
                    'marker': {'colors': ['#ff794d',
                                          '#b32d00',
                                          '#ff8c66']},
                    "labels": [
                        "Agriculture",
                        "Industry",
                        "Services",
                    ],
                    "textposition": "inside",
                    "domain": {"column": 1},
                    "name": "%",
                    "hoverinfo": "label+percent+name",
                    "hole": .4,
                    "type": "pie",
                    'sort': False,
                }],  "layout": {
            "height": 700, "showlegend":False
        },})],className="six columns"),
            html.Div([html.H3('GDP Growth', style = {'textAlign': 'center', 'color': '#ff794d'}),dcc.Graph(
        id='Graph2',
        figure={
            "data": [

                {'y': [120, 130, 125], 'x': [2015, 2016, 2017], 'type': 'bar', 'name': 'Agriculture', 'marker':{'color': ['#ff794d', '#ff794d', '#ff794d']},
                 },
                {'y': [90, 92, 93], 'x': [2015, 2016, 2017], 'type': 'bar', 'name': 'Industry','marker':{'color': ['#b32d00', '#b32d00', '#b32d00']}},
                {'y': [65, 67, 70], 'x': [2015, 2016, 2017], 'type': 'bar', 'name': 'Services', 'marker':{'color': ['#ff8c66', '#ff8c66', '#ff8c66']}}],
             "layout": {
            "height": 700, "annotations": [
        dict(
            x=2015.75,
            y=133,
            xref='x',
            yref='y',
            text='The highest point',
            xanchor='left',
            align='left',
            showarrow=True,
            arrowhead=7,
            font=dict(color='#b32d00'),
            arrowsize=1,
            arrowwidth=2,
            arrowcolor='#b32d00',
            ax=-10,
            ay=-50
        )],
        },'sort': False})], className="six columns"),
    ], className="row")
])

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

dcc.Textarea(
    placeholder='Enter a value...',
    value='This is a TextArea component',
    style={'width': '100%'}
)


#py.iplot(figure, filename='donut')

#app.scripts.config.serve_locally = True

if __name__ == '__main__':
    app.run_server(debug=True, port=8000, host='127.0.0.1')

#