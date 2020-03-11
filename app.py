import dash
import dash_table
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
    dcc.Dropdown(
    id='country_list',
    options=[
        {'label': i, 'value': i} for i in df['Country/Region'].unique()
    ],
    multi=True,
    placeholder="Select a Country",
    ),
    html.Div([
        dcc.Graph(id='confirmed')
        
    ],style = {'width':'50%','float':'left','display': 'inline-block'}),
    html.Div([
        dcc.Graph(id='deaths')
    ],style = {'width':'50%','float':'right','display': 'inline-block'}),
    html.Div([
        dcc.Graph(id='recovered')
    ])
])

print(i for i in df['Country/Region'].unique())
@app.callback(
    Output('confirmed','figure'),
    [Input('country_list','value')]
)
def update_confirmed(country_list):
    



if __name__ == '__main__':
    app.run_server(debug=True)