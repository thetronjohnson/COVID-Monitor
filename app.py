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
            {'label': i, 'value': str(i)} for i in df['Country/Region'].unique()
        ],
        multi=False,
        placeholder="Select a Country",
    ),
    dcc.Graph(id='confirmed'),
    dcc.Graph(id='deaths'),
    dcc.Graph(id='recovered')
        
])

@app.callback(
    Output('confirmed','figure'),
    [Input('country_list','value')]
)
def update_confirmed(country_list):  
    traces = []
    traces.append(dict(
            x = df[df['Country/Region']==country_list]['ObservationDate'],
            y = (df[df['Country/Region']==country_list]['Confirmed']).max(),
            text=f'{country_list}',
            mode='markers',
            opacity=0.7,
            marker=dict(
                    color='rgb(55, 83, 109)'
            ),
        ))

    return {
        'data' :traces,
        'layout': dict(
            xaxis = {'title':'Observation Date'},
            yaxis = {'title':'Confirmed Cases'},
            hovermode='closest',title='COVID-19 Confirmed Cases',
            showlegend=True,
            legend=dict(
                x=1,
                y=1
            ),
            margin=dict(l=40, r=0, t=40, b=30)

        )
    }
@app.callback(
    Output('deaths','figure'),
    [Input('country_list','value')]
)
def update_deaths(country_list):  
    traces = []
    traces.append(dict(
            x = df[df['Country/Region']==country_list]['ObservationDate'],
            y = (df[df['Country/Region']==country_list]['Deaths']).max(),
            text=f'{country_list}',
            mode='markers',
            opacity=0.7,
            marker=dict(
                    color='rgb(55, 83, 109)'
            ),
        ))

    return {
        'data' :traces,
        'layout': dict(
            xaxis = {'title':'Observation Date'},
            yaxis = {'title':'Deaths'},
            hovermode='closest',title='COVID-19 Deaths',
            showlegend=True,
            legend=dict(
                x=1,
                y=1
            ),
            margin=dict(l=40, r=0, t=40, b=30)

        )
    }
@app.callback(
    Output('recovered','figure'),
    [Input('country_list','value')]
)
def update_recovered(country_list):  
    traces = []
    traces.append(dict(
            x = df[df['Country/Region']==country_list]['ObservationDate'],
            y = (df[df['Country/Region']==country_list]['Recovered']).max(),
            text=f'{country_list}',
            mode='markers',
            opacity=0.7,
            marker=dict(
                    color='rgb(55, 83, 109)'
            ),
        ))

    return {
        'data' :traces,
        'layout': dict(
            xaxis = {'title':'Observation Date'},
            yaxis = {'title':'Recovered Cases'},
            hovermode='closest',title='COVID-19 Recovered Cases',
            showlegend=True,
            legend=dict(
                x=1,
                y=1
            ),
            margin=dict(l=40, r=0, t=40, b=30)

        )
    }



if __name__ == '__main__':
    app.run_server(debug=True)