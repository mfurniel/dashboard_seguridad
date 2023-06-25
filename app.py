import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import dash
from dash import Dash, html, dcc, callback
from dash.dependencies import Input, Output, State
import utils as nConst
import graficas as graf
auxx= graf.lineChartCDDA(0,nConst.DELITOS_CON_GRUPOS[nConst.GRUPOS_DELITOS[0]][5])
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
        dcc.Dropdown(
        id='drop1',
        options= nConst.OPCIONES_TERRITORIO,
        value= nConst.DELITOS[0],  # Valor inicial seleccionado
        placeholder='Unidad Territorial', 
        className='custom-dropdown',
        ),
        dcc.Dropdown(
        id='drop2',
        options= nConst.OPCIONES_DELITOS,
        value=nConst.DELITOS[0],  # Valor inicial seleccionado
        placeholder='Delito',
        className='custom-dropdown' 
        ),
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
                        dcc.Graph(
                            id='barrasDelitosNacional',
                            figure=graf.barrasDelitosNacional(False,False)
                        ),
                    ], className='graficotopdelitos'),
                ], className='topmas'),
            ], className='fila'),

            # Fila 1.1
            html.Div([
                html.Div(
                    dcc.Graph(
                        id='lineChartCDDA-nacional',
                        figure=graf.lineChartCDDA(0,nConst.DELITOS_CON_GRUPOS[nConst.GRUPOS_DELITOS[0]][5])
                    ),
                className='nacional1'),
                html.Div([ 
                    dcc.Graph(
                            id='barrasDelitosNacional',
                            figure=graf.ciruclarHvsM('2022','VICTIMA')
                    ),], className='nacional2')
            ], className='fila'),
            # Fila 2
            html.Div([
                html.Div([
                    dcc.Graph(
                        id='lineChartCDDA-region',
                        figure=graf.lineChartCDDA(13,nConst.DELITOS_CON_GRUPOS[nConst.GRUPOS_DELITOS[0]][0])
                    ),
                ], className='regional1'),
                html.Div('Contenido graf 2 region', className='regional2')
            ], className='fila'),
            # Fila 3
            html.Div([
                html.Div([
                    dcc.Graph(
                            id='barrasDelitosNacional',
                            figure=graf.barrasDelitosNacional(True,False)
                    ),    
                ], className='topmenos'),
                html.Div([
                    dcc.Graph(
                            id='barrasDelitosNacional',
                            figure=graf.histogramSxE(18)
                    ),    
                ], className='sexoporedad')
            ], className='fila'),
        ], className='contenido-derecho'),
    ], className='contenido-principal'),
])

@app.callback(
    Output(component_id='lineChartCDDA-nacional', component_property='figure'),
    Input(component_id='drop2', component_property='value')
)
def update_nacional_delito(input_value):
    input_value = input_value.capitalize()
    print(input_value)
    
    # Lógica para actualizar el gráfico según el valor seleccionado en el dropdown
    # Retorna la figura actualizada del gráfico
    fig = graf.lineChartCDDA(0, input_value)
    return fig

@app.callback(
    Output(component_id='lineChartCDDA-region', component_property='figure'),
    Input(component_id='drop2', component_property='value')
)
def update_region_delito(input_value):
    input_value = input_value.capitalize()
    print(input_value)
    
    # Lógica para actualizar el gráfico según el valor seleccionado en el dropdown
    # Retorna la figura actualizada del gráfico
    fig = graf.lineChartCDDA(13, input_value)
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
