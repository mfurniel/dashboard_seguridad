import pandas as pd
import plotly.graph_objects as go
import dash
from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State

def configure_graph1():
    # Configuración del primer gráfico
    delito_buscado = 'Lesiones leves'
    meses = df.columns[1:]
    homicidios = df.loc[delito_buscado]
    fig = go.Figure(data=go.Scatter(x=meses, y=homicidios, mode='lines', marker=dict(symbol='circle', size=8)))
    fig.update_layout(
        title=delito_buscado + '2022 Chile',
        xaxis=dict(title='Meses'),
        yaxis=dict(title='Cantidad de ' + delito_buscado)
    )
    return fig

def configure_graph2():
    # Configuración del segundo gráfico
    df_aux = df.copy()
    df_aux['Total'] = df_aux.sum(axis=1)
    df_aux = df_aux.sort_values("Total", ascending=False)
    listadelitos = df_aux.index[:5].tolist()
    valores_primeros_cinco = df_aux.loc[df_aux.index[:5], 'Total']
    fig = go.Figure(data=go.Bar(x=listadelitos, y=valores_primeros_cinco, width=0.3))
    fig.update_layout(
        title='Top 5 delitos en el año 2022',
        xaxis=dict(title='Delitos'),
        yaxis=dict(title='Cantidad cometida')
    )
    return fig

def linechartnacional():
    delito_buscado = 'Homicidios'
    meses = dap.columns[0:]
    homicidios = dap.loc[delito_buscado]
    homicidios_dad = dad.loc[delito_buscado]
    homicidios_dade = dade.loc[delito_buscado]
    homicidios_dada = dada.loc[delito_buscado]  # Agreg  # Agregar esta línea

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=meses, y=homicidios, mode='lines', name='Casos'))
    fig.add_trace(go.Scatter(x=meses, y=homicidios_dad, mode='lines', name='Detenciones'))  # Agregar esta línea
    fig.add_trace(go.Scatter(x=meses, y=homicidios_dade, mode='lines', name='Denuncias'))
    fig.add_trace(go.Scatter(x=meses, y=homicidios_dada, mode='lines', name='Aprehendidos'))  # Agregar esta línea

    fig.update_layout(
        title=delito_buscado + ' Chile (dap y dad)',  # Actualizar el título
        xaxis=dict(title='Años'),
        yaxis=dict(title='Cantidad de ' + delito_buscado)
    )
    return fig

    

# Cargar los datos
dap = pd.read_excel('dataset/todos-datos-2005-2022.xlsx',sheet_name='casospoliciales')
dap = dap.set_index('GRUPO DELICTUAL / DELITO')
dad = pd.read_excel('dataset/todos-datos-2005-2022.xlsx',sheet_name='detenciones')
dad = dad.set_index('GRUPO DELICTUAL / DELITO')
dade = pd.read_excel('dataset/todos-datos-2005-2022.xlsx',sheet_name='denuncias')
dade = dade.set_index('GRUPO DELICTUAL / DELITO')
dada = pd.read_excel('dataset/todos-datos-2005-2022.xlsx',sheet_name='aprehendidos')
dada = dada.set_index('GRUPO DELICTUAL / DELITO')

df = pd.read_excel('dataset/2022seguridad.xlsx')
df = df.set_index('Delitos')

# Configuración de la aplicación Dash
app = dash.Dash(__name__)

app.layout = html.Div([
    html.Link(href='assets/app.css', rel='stylesheet'),

    # Barra superior
    html.Div([
        html.Link(href='test.css', rel='stylesheet'),
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
                        dcc.Graph(
                            id='delitos-graph',
                            figure=configure_graph2()
                        ),
                    ], className='graficotopdelitos'),
                ], className='topmas'),
            ], className='fila'),

            # Fila 1.1
            html.Div([
                html.Div(
                    dcc.Graph(
                        id='delitos-graph',
                        figure=linechartnacional()
                    ),
                className='nacional1'),
                html.Div('Contenido graf 2 nacion', className='nacional2')
            ], className='fila'),
            # Fila 2
            html.Div([
                html.Div('Contenido graf 1 region', className='regional1'),
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
