import pandas as pd
import plotly.graph_objects as go
import dash
from dash import Dash, html, dcc, callback
from dash.dependencies import Input, Output, State
import utils as nConst
import graficas as graf
import mapa as map

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
        value= '13',  # Valor inicial seleccionado
        placeholder='Unidad Territorial', 
        className='custom-dropdown',
        ),
        dcc.Dropdown(
        id='drop2',
        options= nConst.OPCIONES_DELITOS,
        value=nConst.GRUPOS_DELITOS[0],  # Valor inicial seleccionado
        placeholder=nConst.GRUPOS_DELITOS[0],
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
        html.Div(
            dcc.Graph(
                id='mapachile',
                figure=map.mapChile(),
        ), className='contenido-izquierda'),
        # Columna derecha
        html.Div([
            # Fila 1
            html.Div([
                html.Div([
                    html.Div([                        
                        dcc.Graph(
                            id='barrasDelitosNacional',
                            figure=graf.barrasDelitosNacional(False,'grupos')
                        ),
                        dcc.RadioItems(
                            id='radio-top-barras-callback',
                            options=[
                                {'label':'Grupos', 'value': 'grupos'},
                                {'label':'Delitos de mayor connotación social', 'value': 'Delitos de mayor connotación social'}, 
                                {'label':'Infracción a ley de armas','value': 'Infracción a ley de armas'}, 
                                {'label':'Incivilidades','value': 'Incivilidades'}, 
                                {'label':'Abigeato','value': 'Abigeato'}, 
                                {'label':'Abusos sexuales y otros delitos sexuales','value': 'Abusos sexuales y otros delitos sexuales'}, 
                                {'label':'Violencia intrafamiliar','value': 'Violencia intrafamiliar'}, 
                                {'label':'Receptación','value': 'Receptación'}, 
                                {'label':'Robo frustrado','value': 'Robo frustrado'}, 
                            ],                        
                            value='grupos',  # Valor seleccionado por defecto
                            className='radios-barras-top',
                        )
                    ], className='graficotopdelitos'),
                ], className='topmas'),
            ], className='fila'),

            # Fila 1.1
            html.Div([
                html.Div(
                    dcc.Graph(
                        id='lineChartCDDA-nacional',                      
                        figure=graf.lineChartCDDA(0,nConst.GRUPOS_DELITOS[0])
                    ),
                className='nacional1'),
                html.Div([ 
                    dcc.Graph(
                            id='lineChartCDDA-region',                          
                            figure=graf.lineChartCDDA(13,nConst.GRUPOS_DELITOS[0])
                    ),], className='nacional2')
            ], className='fila'),
            # Fila 2
            html.Div([
                html.Div([
                    dcc.Graph(
                        id='circular-barra-victima',
                        figure=graf.ciruclarHvsM('2018','VICTIMA',17)
                    ),
                ], className='regional1'),
                html.Div(
                    dcc.Graph(
                        id='circular-barra-vitimario',
                        figure=graf.ciruclarHvsM('2018','VICTIMARIO',17)
                    ), className='regional2'),
                # html.Div([
                #     dcc.Graph(
                #         id='circular-barra-victima',
                #         figure=graf.ciruclarHvsM('2018','VICTIMA',17)
                #     ),
                # ], className='regional1'),
                # html.Div(
                #     dcc.Graph(
                #         id='circular-barra-vitimario',
                #         figure=graf.ciruclarHvsM('2018','VICTIMARIO',17)
                #     ), className='regional2')
            ], className='fila'),
            # Fila 3
            html.Div([
                html.Div([
                    dcc.Graph(
                            id='histogramaSE',
                            figure=graf.histogramSxE(17)
                    ),    
                ], className='histoSE'),
            # html.Div('Contenido graf 2 inmigracion', className='inmigracion')
            ], className='filasingular'),
        ], className='contenido-derecho'),
    ], className='contenido-principal'),
])

@app.callback(
    Output(component_id='lineChartCDDA-nacional', component_property='figure'),
    Input(component_id='drop2', component_property='value')
)
def update_nacional_delito(input_value):
    input_value = input_value.capitalize()
    
    
    # Lógica para actualizar el gráfico según el valor seleccionado en el dropdown
    # Retorna la figura actualizada del gráfico
    fig = graf.lineChartCDDA(0, input_value)
    return fig

@app.callback(
    Output(component_id='lineChartCDDA-region', component_property='figure'),
    [Input(component_id='drop2', component_property='value'),
     Input(component_id='drop1', component_property='value')]
)
def update_nacional_delito(input_value1, input_value2):
    input_value1 = input_value1.capitalize()
    input_value2 = input_value2.capitalize()
    
    # Lógica para actualizar el gráfico según los valores seleccionados en los dropdowns
    # Retorna la figura actualizada del gráfico
    fig = graf.lineChartCDDA(input_value2, input_value1)
    return fig

@app.callback(
    Output('barrasDelitosNacional', 'figure'),
    [Input('radio-top-barras-callback', 'value')]
)
def update_output(value):
    return graf.barrasDelitosNacional(False,value)
    


if __name__ == '__main__':
    app.run_server(debug=True)
