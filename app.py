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
    dash_table.DataTable(
        id = 'covid-table',
        columns = [
            {"name":i,"id":i,"selectable":True} for i in df.columns
        ],
        data=df.to_dict('records'),
        editable=True,
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        column_selectable="single",
        row_selectable="multi",
        selected_columns=[],
        selected_rows=[],
        page_action="native",
        page_current= 0,
        page_size= 10,
    ),
    html.Div(id='datatable-interactivity-container')
])

if __name__ == '__main__':
    app.run_server(debug=True)