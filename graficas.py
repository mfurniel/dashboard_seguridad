import pandas as pd
import utils as nConst
import plotly.graph_objects as go
import plotly.express as px

#Grefica Top X Delitos o Grupos Delictuales

def barrasDelitosNacional(ascendente,grupo):
     
    # Leer el archivo de Excel especificado en nConst.EXCEL_PATH[0] y almacenar los datos en un DataFrame
    df = pd.read_excel(nConst.EXCEL_PATH[0]) # nConst.EXCEL_PATH[0] es 'nacional'

    # Establecer la columna 'GRUPO DELICTUAL / DELITO' como índice del DataFrame
    
    df = df.set_index('GRUPO DELICTUAL / DELITO')

    if grupo == 'grupos':
        df = df[~df.index.isin(nConst.DELITOS)]
    elif nConst.DELITOS_CON_GRUPOS[grupo]==[]:
        df=pd.DataFrame(df.loc[grupo]).T
    else:
        df = df[~df.index.isin(nConst.GRUPOS_DELITOS)]
        for i, grupo_delito in enumerate(nConst.GRUPOS_DELITOS):
            if grupo == grupo_delito and nConst.DELITOS_CON_GRUPOS[grupo_delito]:
                df = df[df.index.isin(nConst.DELITOS_CON_GRUPOS[grupo_delito])]
                break  
    #   
    # Copiar el DataFrame original para realizar modificaciones sin afectar los datos originales
    df_aux = df.copy()
    
    # Agregar una columna 'Total' que contenga la suma de todas las filas
    df_aux['Total'] = df_aux.sum(axis=1)


    # Ordenar el DataFrame en función de los valores de la columna 'Total' de forma descendente
    df_aux = df_aux.sort_values("Total", ascending=ascendente)
    
    # Obtener una lista de los cinco delitos más comunes
    listadelitos = df_aux.index.tolist()
   
    # Obtener los valores correspondientes a los cinco delitos más comunes en la columna 'Total'
    valores_primeros_cinco = df_aux.loc[df_aux.index, 'Total']

    
    # Crear el objeto de la figura del gráfico de barras utilizando la biblioteca plotly.graph_objects
    fig = go.Figure(data=go.Bar(x=listadelitos, y=valores_primeros_cinco, width=0.3))
    
    # Configurar el diseño del gráfico, incluyendo título y etiquetas de los ejes
    grupo_o_delito=''
    if grupo:
        grupo_o_delito='Delitos'
    else:
        grupo_o_delito='Grupos de Delitos'

    cometidos=''
    if ascendente:
        cometidos='menos'
    else:
        cometidos='más'

    fig.update_layout(
        title='Top ' + grupo_o_delito + ' ' + cometidos +' Cometidos (2005-2022)',
        xaxis=dict(title='Delitos'),
        yaxis=dict(title='Cantidad cometida')
    )

    if grupo!='grupos' and nConst.DELITOS_CON_GRUPOS[grupo]==[]:
       fig.update_yaxes(range=[0, 200000])  # Establecer el rango del eje y de 0 a 10000 (puedes ajustar el valor según tus necesidades)

    # Devolver la figura del gráfico generada
    return fig

# Grafico LineChart Nacional o Regional se ocupa la misma funcion

def lineChartCDDA(numero_territorio,delito_buscado):
    numero_territorio=int(numero_territorio)
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

    conector=''
    if(numero_territorio==0):
        conector=' en '
    else:
        conector=' en la '

    fig.update_layout(
        title=delito_buscado + conector + nConst.TERRITORIO[numero_territorio],
        xaxis=dict(title='Años'),
        yaxis=dict(title='Cantidad de ' + delito_buscado)
    )
    return fig

def ciruclarHvsM(año,tipo):
    df = pd.read_excel('dataset/nacional/sexo_edad_nacional.xlsx')
    filtro = (df['Tipo Participante'] == tipo) & (df['Sexo'] == 'MUJER') & (df['Edad'] == 'Total')
    fila_filtrada = df[filtro]
    valorM = fila_filtrada[año].values[0]
    filtro = (df['Tipo Participante'] == tipo) & (df['Sexo'] == 'HOMBRE') & (df['Edad'] == 'Total')
    fila_filtrada = df[filtro]
    valorH = fila_filtrada[año].values[0]
    # Etiquetas para las categorías
    labels = ['Hombres', 'Mujeres']

    # Valores para cada categoría
    values = [valorH, valorM]

    # Crear el gráfico circular
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

    # Personalizar el diseño
    fig.update_traces(hole=0.4, hoverinfo="label+percent+value")

    # Añadir título
    fig.update_layout(title_text= tipo + " Hombres vs Mujeres todos los Delitos Año "+año)

    # Mostrar el gráfico
    return fig

def histogramSxE(numero_territorio):
    df = pd.read_excel(nConst.EXCEL_PATH[numero_territorio])
    #if(numero_territorio == 17):
    listafiltrada = df[df['Edad'] != 'Total']
    listafiltrada = listafiltrada[listafiltrada['Sexo'] == 'TOTAL']
    listafiltrada = listafiltrada[listafiltrada['Tipo Participante'] == 'VICTIMA']

    df_melted = pd.melt(listafiltrada, id_vars=['Edad'], var_name='Año', value_name='Cantidad')
    fig = px.histogram(df_melted, x='Edad', y='Cantidad', color='Año', category_orders={'Año': [2005, 2022]})
    fig.update_layout(
    title='Histograma de Víctimas de Delitos por Edades',
    xaxis_title='Cantidad de Víctimas',
    yaxis_title='Frecuencia',
    barmode='group'
    )
    return fig

# import geopandas as gpd


# def mapachile():
#     # Cargar los datos geoespaciales de Chile
#     chile = gpd.read_file('regiones_edit.geojson')

#     # Crear el gráfico de Chile con Plotly
#     fig = px.choropleth(chile, geojson=chile.geometry, locations=chile.index,
#                         color='color_column',  # Columna que determina los colores del mapa
#                         projection="natural earth")

#     # Personalizar el gráfico
#     fig.update_layout(title_text='Mapa de Chile')
    
#     return fig