import pandas as pd
import plotly.graph_objects as go
import dash # a
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.io as pio


df = pd.read_excel('dataset/2022seguridad.xlsx')
df_melted = pd.melt(df, var_name='Mes', value_name='Valor')

fig = px.pie(df, values='diciembre', names='Delitos')


app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Gráfico de Delitos'),
    dcc.Graph(
        id='delitos-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)