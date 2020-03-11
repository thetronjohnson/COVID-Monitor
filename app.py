import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output
import os

BASE_DIR = os.getcwd()

COVID =  os.path.join(BASE_DIR,'Datasets/covid_19_data.csv')



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv(COVID)

app.layout = html.Div([
    dcc.Graph(id='death-tolls'),
    dcc.Slider(
        id='date-slider',
        min = df['ObservationDate'].min(),
        max = df['ObservationDate'].max(),
        value = df['ObservationDate'].min(),
        marks={str(date): str(date) for date in df['ObservationDate'].unique()},
        step = None
    )
])

@app.callback(
    Output('death-tolls','figure'),
    [Input('date-slider','value')]
)
def update_figure(selected_date):
    filtered_df = df[df.year == selected_date]
    traces = []
    for i in filtered_df['Country/Region'] .unique():
        df_by_region = filtered_df[filtered_df['Country/Region']  == i]
        traces.append(dict(
            x=df[df['Country/Region'] == i]['ObservationDate'],
            y=df[df['Country/Region'] == i]['Deaths'],
            mode='markers',
            opacity=0.7,
            marker={
            'size': 15,
            'line': {'width': 0.5, 'color': 'white'}
            },
            name=i
        ))

    return {
        'data': traces,
        'layout': dict(
            xaxis={'type': 'log', 'title': 'GDP Per Capita',
                   'range':[2.3, 4.8]},
            yaxis={'title': 'Life Expectancy', 'range': [20, 90]},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            hovermode='closest',
            transition = {'duration': 500},
        )
    }

'''
app.layout = html.Div([
    dcc.Graph(
        id='COVID-19',
        figure={
            'data': [
                dict(
                    x=df[df['Country/Region'] == i]['ObservationDate'],
                    y=df[df['Country/Region'] == i]['Deaths'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df['Country/Region'].unique() 
            ],
            'layout': dict(
                xaxis={'title': 'Date'},
                yaxis={'title': 'Deaths'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])
'''

if __name__ == '__main__':
    app.run_server(debug=True)