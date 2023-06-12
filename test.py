import dash
from dash import html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Mi Aplicación Dash'),
    html.Div('Haz clic en el botón para mostrar/ocultar la barra lateral:'),
    html.Button('Toggle Sidebar', id='toggle-button'),
    html.Div(id='sidebar', children=[
        html.P('Texto 1'),
        html.P('Texto 2'),
        html.P('Texto 3'),
    ]),
    # Resto de los componentes de tu aplicación
])

@app.callback(Output('sidebar', 'style'), [Input('toggle-button', 'n_clicks')])
def toggle_sidebar(n_clicks):
    if n_clicks is None:
        return {'transform': 'translateX(-200px)'}
    elif n_clicks % 2 == 0:
        return {'transform': 'translateX(-200px)'}
    else:
        return {'transform': 'translateX(0)'}

if __name__ == '__main__':
    app.run_server(debug=True)
