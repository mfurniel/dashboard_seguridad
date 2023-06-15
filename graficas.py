import pandas as pd
import utils as nConst
import plotly.graph_objects as go

#Grefica Top X Delitos o Grupos Delictuales

def configure_graph():
    
    df = pd.read_excel('dataset/2022seguridad.xlsx')
    df = df.set_index('Delitos')
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

# Grafico LineChart Nacional o Regional se ocupa la misma funcion

def lineChartCDDA(numero_territorio,delito_buscado):
    excel_path = nConst.EXCEL_PATH[numero_territorio]
    subcategorias = nConst.SUBCATEGORIAS

    casos_policiales = pd.read_excel(excel_path, sheet_name=subcategorias[0]).set_index('GRUPO DELICTUAL / DELITO')
    denuncias = pd.read_excel(excel_path, sheet_name=subcategorias[1]).set_index('GRUPO DELICTUAL / DELITO')
    detenciones = pd.read_excel(excel_path, sheet_name=subcategorias[2]).set_index('GRUPO DELICTUAL / DELITO')
    aprehendidos = pd.read_excel(excel_path, sheet_name=subcategorias[3]).set_index('GRUPO DELICTUAL / DELITO')

    años = casos_policiales.columns[0:]
    homicidios = casos_policiales.loc[delito_buscado]
    homicidios_detenciones = detenciones.loc[delito_buscado]
    homicidios_denuncias = denuncias.loc[delito_buscado]
    homicidios_aprehendidos = aprehendidos.loc[delito_buscado]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=años, y=homicidios, mode='lines', name='Casos'))
    fig.add_trace(go.Scatter(x=años, y=homicidios_detenciones, mode='lines', name='Detenciones'))
    fig.add_trace(go.Scatter(x=años, y=homicidios_denuncias, mode='lines', name='Denuncias'))
    fig.add_trace(go.Scatter(x=años, y=homicidios_aprehendidos, mode='lines', name='Aprehendidos'))

    fig.update_layout(
        title=delito_buscado + ' en ' + nConst.TERRITORIO[numero_territorio],
        xaxis=dict(title='Años'),
        yaxis=dict(title='Cantidad de ' + delito_buscado)
    )
    return fig

