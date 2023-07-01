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
        value='Delitos de mayor connotación social',  # Valor inicial seleccionado
        placeholder='Grupo Delictual o Delito',
        className='custom-dropdown' 
        ),
        dcc.Dropdown(
        id='drop3',
        options= nConst.OPCIONES_ANYOS,
        value='2022',  # Valor inicial seleccionado
        placeholder='Año',
        className='custom-dropdown' 
        ),
        html.Div([
            html.Span('Ultima Actualización: 30/06/2023'),
            html.Span('Datos: CEAD "Centro de Estudios y Análisis del Delito"'),
        ], className='info'),
    ], className='barra-superior'),

    # Contenido principal
    html.Div([
        # Columna izquierda
        # html.Div(
        #     dcc.Graph(
        #         id='mapachile',
        #         figure=map.mapChile(),
        # ), className='contenido-izquierda'),
        # Columna derecha
        html.Div([
            # Fila 1
            html.Div([
              
                    html.Div(
                    dcc.Graph(
                        id='mapachile',
                        figure=map.mapChile(),
                    ), className='contenido-izquierda'),
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
                
            ], className='fila'),

            # Fila 1.1
            html.Div([
                html.Div(
                    dcc.Graph(
                        id='lineChartCDDA-nacional',                      
                        figure=graf.lineChartCDDA(0,nConst.GRUPOS_DELITOS[0])
                    ),
                className='nacionalline'),
                html.Div([ 
                    dcc.Graph(
                            id='lineChartCDDA-region',                          
                            figure=graf.lineChartCDDA(13,nConst.GRUPOS_DELITOS[0])
                    ),], className='regionalline')
            ], className='fila'),
            # Fila 2
            html.Div([
                html.Div([
                    dcc.Graph(
                        id='circularbarravictimanacional',
                        figure=graf.ciruclarHvsM('2022','VICTIMA',0)
                    ),
                ], className='cNacionalva'),
                html.Div(
                    dcc.Graph(
                        id='circularbarravictimarionacional',
                        figure=graf.ciruclarHvsM('2022','VICTIMARIO',0)
                    ), className='cNacionalvo'),
                html.Div([
                    dcc.Graph(
                        id='circularbarravictimaregional',
                        figure=graf.ciruclarHvsM('2022','VICTIMA',13)
                    ),
                ], className='cRegionalva'),
                html.Div(
                    dcc.Graph(
                        id='circularbarravictimarioregional',
                        figure=graf.ciruclarHvsM('2022','VICTIMARIO',13)
                    ), className='cRegionalvo')
            ], className='fila'),
            # Fila 3
            html.Div([
                html.Div([
                    dcc.Graph(
                            id='histogramaSE',
                            figure=graf.histogramSxE(0,'VICTIMA')
                    ),    
                ], className='histoSE'),
            # html.Div('Contenido graf 2 inmigracion', className='inmigracion')
            ], className='filasingular'),
             html.Div([
                html.Div([
                    dcc.Graph(
                            id='histogramaSEvictiamrios',
                            figure=graf.histogramSxE(0,'VICTIMARIO')
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
    
from dash.dependencies import Output, Input

@app.callback(
    [Output(component_id='circularbarravictimanacional', component_property='figure'),
     Output(component_id='circularbarravictimarionacional', component_property='figure'),
     Output(component_id='circularbarravictimaregional', component_property='figure'),
     Output(component_id='circularbarravictimarioregional', component_property='figure')],
     [Input(component_id='drop1', component_property='value'),
     Input(component_id='drop3', component_property='value')]
)
def updateciculos(input_value1, input_value2):
    # print(input_value1)
    # print(input_value2)
    # Lógica para actualizar las propiedades de los cuatro outputs según el valor del input
    # Retorna los valores actualizados para cada una de las propiedades de los outputs
    valor1 = graf.ciruclarHvsM(input_value2,'VICTIMA',0)
    valor2 = graf.ciruclarHvsM(input_value2,'VICTIMARIO',0)
    valor3 = graf.ciruclarHvsM(input_value2,'VICTIMA',input_value1)
    valor4 = graf.ciruclarHvsM(input_value2,'VICTIMARIO',input_value1)
    return valor1, valor2, valor3, valor4

@app.callback(
    Output(component_id='histogramaSE', component_property='figure'),
    Input(component_id='drop1', component_property='value')
)
def upadte_histo(input_value):
    fig = graf.histogramSxE(input_value)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
