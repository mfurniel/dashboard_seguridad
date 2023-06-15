import pandas as pd
import plotly.graph_objects as go
import dash
from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State
import utils as nConst
import graficas as graf

# def configure_graph1():
#     # Configuración del primer gráfico
#     delito_buscado = 'Lesiones leves'
#     meses = df.columns[1:]
#     homicidios = df.loc[delito_buscado]
#     fig = go.Figure(data=go.Scatter(x=meses, y=homicidios, mode='lines', marker=dict(symbol='circle', size=8)))
#     fig.update_layout(
#         title=delito_buscado + '2022 Chile',
#         xaxis=dict(title='Meses'),
#         yaxis=dict(title='Cantidad de ' + delito_buscado)
#     )
#     return fig

# Configuración de la aplicación Dash
app = dash.Dash(__name__)

app.layout = html.Div([
    html.Link(href='assets/app.css', rel='stylesheet'),

    # Barra superior
    html.Div([
        html.Link(href='app.css', rel='stylesheet'),
        html.Div([html.H1('Dataviz Security')], className='logo'),
        html.Div([
            html.Span('Ultima Actualización: 01/06/2023'),
            html.Span('Datos: CEAD "Centro de Estudios y Análisis del Delito"'),
        ], className='info'),
    ], className='barra-superior'),

    # Contenido principal
    html.Div([
        # Columna izquierda
        html.Div('Contenido columna izquierda', className='contenido-izquierda'),

        # Columna derecha
        html.Div([
            # Fila 1
            html.Div([
                html.Div([
                    html.Div([
                        # html.H1(children='Top 5 delitos mas cometidos'),
                        # dcc.Graph(
                        #     id='delitos-graph',
                        #     figure=configure_graph2()
                        # ),
                    ], className='graficotopdelitos'),
                ], className='topmas'),
            ], className='fila'),

            # Fila 1.1
            html.Div([
                html.Div(
                    dcc.Graph(
                        id='delitos-graph',
                        figure=graf.lineChartCDDA(0,nConst.DELITOS[nConst.GRUPOS_DELITOS[0]][5])
                    ),
                className='nacional1'),
                html.Div('Contenido graf 2 nacion', className='nacional2')
            ], className='fila'),
            # Fila 2
            html.Div([
                html.Div([
                    dcc.Graph(
                        id='delitos-graph',
                        figure=graf.lineChartCDDA(13,nConst.DELITOS[nConst.GRUPOS_DELITOS[0]][0])
                    ),
                ], className='regional1'),
                html.Div('Contenido graf 2 region', className='regional2')
            ], className='fila'),
            # Fila 3
            html.Div([
                html.Div('Contenido graf 1 top menos', className='topmenos'),
                html.Div('Contenido graf 2 inmigracion', className='inmigracion')
            ], className='fila'),
        ], className='contenido-derecho'),
    ], className='contenido-principal'),
])

if __name__ == '__main__':
    app.run_server(debug=True)
