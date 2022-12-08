import numpy as np
import pandas as pd
import plotly.graph_objects as go
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input,Output

# Write Pandas code here

patients=pd.read_csv('IndividualDetails.csv')

total=patients.shape[0]
active=patients[patients['current_status']=='Hospitalized'].shape[0]
recovered=patients[patients['current_status']=='Recovered'].shape[0]
deaths=patients[patients['current_status']=='Deceased'].shape[0]

pbar=patients.groupby('detected_state').count()['id'].reset_index()

main=pd.read_csv('covid_19_india.csv')
main['total']=main['ConfirmedIndianNational'] + main['ConfirmedForeignNational']
main['total']=np.cumsum(main['total'].values)

age=pd.read_csv('AgeGroupDetails.csv')


# external CSS stylesheets
external_stylesheets = [
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    }
]

options=[
    {'label':'Hospitalized', 'value':'Hospitalized'},
    {'label':'Recovered', 'value':'Recovered'},
    {'label': 'Deceased', 'value':'Deceased'}
]


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout=html.Div([
    html.H1("CoronaVirus - India'a Perspective", className="text-white mt-50 text-center"),
    html.Div([

        html.Div([
            html.Div([
                html.Div([
                    html.H3("Total Cases", className="text-white"),
                    html.H4(total,className="text-white")
                ],className="card-body")
            ],className="card bg-danger")
        ],className="col-md-3"),

        html.Div([
            html.Div([
                html.Div([
                    html.H3("Active", className="text-white"),
                    html.H4(active,className="text-white")
                ],className="card-body")
            ],className="card bg-info")
        ],className="col-md-3"),

        html.Div([
            html.Div([
                html.Div([
                    html.H3("Recovered", className="text-white"),
                    html.H4(recovered,className="text-white")
                ],className="card-body")
            ],className="card bg-warning")
        ],className="col-md-3"),

        html.Div([
            html.Div([
                html.Div([
                    html.H3("Deaths", className="text-white"),
                    html.H4(deaths,className="text-white")
                ],className="card-body")
            ],className="card bg-success")
        ],className="col-md-3")

    ],className="row", style={'margin-top':'50px'}),

    html.Div([

        html.Div([
            html.Div([
                html.Div([
                    dcc.Graph(id='Line Plot',
                              figure={'data':[go.Scatter(x=main['Date'], y=main['total'],mode='lines')],
                                      'layout':go.Layout(title='Day by Day Analysis',xaxis={'title':'Date'},yaxis={'title':'Number of Cases'})})
                ], className='card-body')
            ],className='card')
        ], className='col-md-8'),
        html.Div([
            html.Div([
               html.Div([
                   dcc.Graph(id='pie',
                             figure={'data':[go.Pie(labels=age['AgeGroup'],values=age['TotalCases'])],
                                     'layout':go.Layout(title='Age Distribution')})
               ], className='card-body')
            ], className="card")
        ], className='col-md-4')

    ], className="row", style={'margin-top':'50px'}),

    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id='picker', options=options, value='All'),
                    dcc.Graph(id='bar')
                ], className='card-body')
            ], className='card')
        ], className='col-md-12')
    ], className='row', style={'margin-top':'50px'})


],className="container")

@app.callback(Output('bar','figure'),
              [Input('picker','value')])
def update_figure(type):

    if type=="All":
        pbar = patients.groupby('detected_state').count()['id'].reset_index()
    else:
        new = patients[patients['current_status'] == type]
        pbar = new.groupby('detected_state').count()['id'].reset_index()

    return {'data':[go.Bar(x=pbar['detected_state'],y=pbar['id'])],
            'layout':go.Layout(title='Bar Chart')}


if __name__=="__main__":
    app.run_server(debug=True)