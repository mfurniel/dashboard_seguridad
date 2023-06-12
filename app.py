import pandas as pd
import plotly.graph_objects as go
import dash
from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State

df = pd.read_excel('dataset/2022seguridad.xlsx')
df = df.set_index('Delitos')
delito_buscado='Lesiones leves'
meses = df.columns[1:]
homicidios = df.loc[delito_buscado]
fig = go.Figure(data=go.Scatter(x=meses, y=homicidios, mode='lines', marker=dict(symbol='circle', size=8)))
fig.update_layout(
    title=delito_buscado + '2022 Chile',
    xaxis=dict(title='Meses'),
    yaxis=dict(title='Cantidad de ' + delito_buscado)
)

app = dash.Dash(__name__)

# Crear el diseño de la aplicación
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),  # Componente para almacenar la URL actual
    
    # Barra superior
    html.Link(href='assets/test.css', rel='stylesheet'),
    html.Div([
        html.Link(href='test.css', rel='stylesheet'),
        html.Div([html.H1('Dataviz Security')], className='logo'),
        
        html.A('NACIONAL', href='/', className='opcion lateral'),  # Enlace a la página "NACIONAL"
        html.A('REGIONES', href='/regiones', className='opcion lateral'),  # Enlace a la página "REGIONES"
        html.A('DELITOS', href='/delitos', className='opcion lateral'),  # Enlace a la página "DELITOS"
        html.A('VARIOS', href='/varios', className='opcion lateral'),  # Enlace a la página "VARIOS"
        html.Div([
            html.Span('Ultima Actualización: 01/06/2023'),
            html.Span('Datos: CEAD "Centro de Estudios y Análisis del Delito"'),
        ], className='info'),
    ], className='barra-superior'),

    html.Div(id='page-content')  # Contenedor para el contenido de la página
])

# Callback para cambiar el contenido de la página según la URL
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return html.Div([
                html.Div([
                    html.H1(children='Homicidios 2022 a Nivel Nacional'),
                    dcc.Graph(
                        id='delitos-graph',
                        figure=fig
                    ),
                ], className='col-6'),

                html.Div([
                    html.H1(children='Homicidios 2022 Region Metropolitana'),
                    dcc.Graph(
                        id='delitos-graph',
                        figure=fig
                    ),
                ], className='col-6')
            ], className='row')
    elif pathname == '/regiones':
        return html.Div([
            html.H1(children='Homicidios 2022 Región Metropolitana'),
            dcc.Graph(
                id='delitos-graph-regiones',
                figure=fig
            ),
        ], className='col-6')
    elif pathname == '/delitos':
        # Código para la página "DELITOS"
        return html.Div([
            html.H1(children='Página de Delitos')
        ])
    elif pathname == '/varios':
        # Código para la página "VARIOS"
        return html.Div([
            html.H1(children='Página de Varios')
        ])
    else:
        # Página por defecto (por ejemplo, la página "NACIONAL")
        return html.Div([
            html.H1(children='Homicidios 2022 a Nivel Nacional'),
            dcc.Graph(
                id='delitos-graph-nacional',
                figure=fig
            ),
        ], className='col-6')

if __name__ == '__main__':
    app.run_server(debug=True)
