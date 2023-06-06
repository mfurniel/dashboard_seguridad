import pandas as pd
import plotly.graph_objects as go
import dash
from dash import dcc, html
from dash.dependencies import Input, Output


df = pd.read_excel('dataset/2022seguridad.xlsx')

fig = go.Figure(data=[
    go.Bar(name='enero', x=df['Delitos'], y=df['enero']),
    go.Bar(name='febrero', x=df['Delitos'], y=df['febrero'])
])

fig2 = go.Figure(data=[go.Pie(labels=df['Delitos'], values=df['enero'])])


app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Gráfico de Delitos'),
    dcc.Graph(
        id='delitos-graph',
        figure=fig
    ),
    dcc.Graph(
        id='delitos2-graph',
        figure=fig2
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)