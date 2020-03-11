import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import os

BASE_DIR = os.getcwd()

COVID =  os.path.join(BASE_DIR,'Datasets/covid_19_data.csv')



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv(COVID)

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

if __name__ == '__main__':
    app.run_server(debug=True)