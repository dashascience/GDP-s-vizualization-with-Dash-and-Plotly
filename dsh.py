
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_auth
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd

VALID_USERNAME_PASSWORD_PAIRS = [['hello', 'dasha']]

app = dash.Dash()
colors = {'background': '#ffffff','text': '#B22222'}

auth = dash_auth.BasicAuth(app,VALID_USERNAME_PASSWORD_PAIRS)

dane = pd.read_csv('dane.txt')
app.layout = html.Div(style={'backgroundColor': colors['background']},
                      children=[
                          html.H1(children='Ukrainian gross domestic product (GDP)',style={'textAlign': 'center','color': colors['text']}),
                          html.Div(id='subtitle', children='Current US$', style={'textAlign': 'center','color': colors['text'], 'fontSize': 25}),
                          dcc.Dropdown(
                                             id='dropdown',
                                             options=[{'label': i, 'value': i} for i in list(dane.year)],
                                             value= 2016),
                      ])


app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

@app.callback(dash.dependencies.Output('subtitle', 'children'),
              [dash.dependencies.Input('dropdown', 'value')])
def update_plot(value):

    return html.Div([
                               html.Div([html.H3('Major Sectors', style = {'textAlign': 'center', 'color': '#ff794d'}),
                                          dcc.Graph(id='Graph1',
                                                    figure={ "data": [{"values": [int(dane[dane.year == value].agriculture),
                                                                                  int(dane[dane.year == value].industry),
                                                                                  int(dane[dane.year == value].services)],
                                                                       'marker': {'colors': ['#ff794d','#b32d00','#ff8c66']},
                                                                       "labels": ["Agriculture","Industry","Services",],
                                                                       "textposition": "inside",
                                                                       "domain": {"column": 1},
                                                                       "name": "%",
                                                                       "hoverinfo": "label+percent+name",
                                                                       "hole": .4,
                                                                       "type": "pie",
                                                                       'sort': False,}],
                                                             "layout": {"height": 700, "showlegend":False},})],
                                         className="six columns"),
                              html.Div([html.H3('GDP Growth', style = {'textAlign': 'center', 'color': '#ff794d'}),
                                        dcc.Graph(id='Graph2',
                                                  figure={"data": [{'y': [120, 130, 125],
                                                                    'x': [2015, 2016, 2017],
                                                                    'type': 'bar',
                                                                    'name': 'Agriculture',
                                                                    'marker':{'color': ['#ff794d', '#ff794d', '#ff794d']},},
                                                                    {'y': [90, 92, 93],
                                                                     'x': [2015, 2016, 2017],
                                                                    'type': 'bar',
                                                                     'name': 'Industry',
                                                                     'marker':{'color': ['#b32d00', '#b32d00', '#b32d00']}},
                                                                     {'y': [65, 67, 70],
                                                                     'x': [2015, 2016, 2017],
                                                                    'type': 'bar',
                                                                    'name': 'Services',
                                                                    'marker':{'color': ['#ff8c66', '#ff8c66', '#ff8c66']}}],
                                                        "layout": {"height": 700, "annotations": [dict( x=2015.75,
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
                                                                                                        ay=-50)],
                                                                   },'sort': False})], className="six columns"),], className="row")

#
# @app.callback(
#     dash.dependencies.Output('Graph1-button-basic', 'children'),
#     [dash.dependencies.Input('button1', 'n_clicks')],
#     [dash.dependencies.State('input-box', 'value')])
# def update_output(n_clicks, value):
#     return 'The input value was "{}" and the button has been clicked {} times'.format(
#         value,
#         n_clicks
#     )

if __name__ == '__main__':
    app.run_server(debug=True, port=8000, host='127.0.0.1')

