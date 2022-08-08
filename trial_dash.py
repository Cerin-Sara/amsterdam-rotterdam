import dash
from dash import dcc
from dash import html
app=dash.Dash()
app.layout=html.Div([
    html.H1('Analysis of Iris data using scatter matrix'),
    html.Div('Data Science Dashboard'),
    ])

if __name__=='__main__':
    app.run_server(port=4050,debug=True)


from dash import dcc
dcc.Slider(value=4, min=-10, max=20, step=0.5,)
from dash import dcc, html, Input, Output
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Slider(0, 20, 5,
               value=10,
               id='my-slider'
    ),
    html.Div(id='slider-output-container')
])

@app.callback(
    Output('slider-output-container', 'children'),
    Input('my-slider', 'value'))
def update_output(value):
    return 'You have selected "{}"'.format(value)

if __name__ == '__main__':
    app.run_server(debug=True)


# from dash import dcc

# # Slider has included=True by default
# dcc.Slider(0, 100, value=65,
#     marks={
#         0: {'label': '0°C', 'style': {'color': '#77b0b1'}},
#         26: {'label': '26°C'},
#         37: {'label': '37°C'},
#         100: {'label': '100°C', 'style': {'color': '#f50'}}
#     }
# )
