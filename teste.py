import dash
import dash_html_components as html
import dash_core_components as dcc
import numpy as np
import plotly.graph_objs as go

np.random.seed(50)
x_rand = np.random.randint(1,61,60)
y_rand = np.random.randint(1,61,60)

app = dash.Dash()

app.layout= html.Div(
    dcc.Graph(
        id='scatter_chart',
        figure={
            'data': [
                go.Scatter(
                    x=x_rand,
                    y= y_rand,
                    mode='markers'
                )
            ],
            'layout': go.Layout(
                title= 'scatter plots of random 60',
                xaxis ={'title': 'random x values'},
                yaxis ={'title': 'random y values'},
                width= 700
            )
        },
        style={'overflow-y':'scroll','width':100}
    )
    )

if __name__ =='__main__':
    app.run_server()