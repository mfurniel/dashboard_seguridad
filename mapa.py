import pandas as pd
import requests
import plotly.express as px

def mapChile():
    regions = ['Región de Arica y Parinacota', 'Región de Tarapacá', 'Región de Antofagasta', 'Región de Magallanes y Antártica Chilena',
            'Región de Aysén del Gral.Ibañez del Campo', 'Región de Atacama', "Región de Coquimbo", 'Región de Valparaíso',
            'Región Metropolitana de Santiago', 'Región de Los Lagos', 'Región de Los Ríos', 'Región de La Araucanía', 'Región del Bío-Bío', 
            'Región de Ñuble', 'Región del Maule', 'Región del Libertador Bernardo O\'Higgins']

    # Como ejemplo, creamos un dataframe con los nombres descritos en regions, llenando los campos de la columna NAME_REG
    df = pd.DataFrame(regions, columns=['NAME_REG'])

    # Para demostración, creamos una columna con la longitud del nombre de la región
    df['name_length'] = df['NAME_REG'].str.len()

    # Leemos los datos del GeoJSON de los límites regionales de Chile desde GitHub
    repo_url = 'https://raw.githubusercontent.com/caracena/chile-geojson/master/regiones.json'
    chile_regions_geo = requests.get(repo_url).json()

    # Coroplético que representa la longitud de los nombres de las regiones de Chile
    fig = px.choropleth(data_frame=df,
                        geojson=chile_regions_geo, 
                        locations='NAME_REG', # nombre de la columna relevante del dataframe
                        featureidkey='properties.Region',  # ruta del campo del feature de GeoJSON con cuyos valores se cotejan los valores de la columna relevante
                        color='name_length',
                        color_continuous_scale="plasma",
                        scope="south america",
                    )
    fig.update_geos(showcountries=False, showcoastlines=False, showland=False, fitbounds="locations")
    # fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.update_layout(
        # autosize=False, 
        # margin=dict(l=0, r=0, t=0, b=0),  # Ajusta los márgenes del gráfico
        height=500,  # Establece la altura del gráfico en píxeles
        width=335,
    )
    fig.update_layout(coloraxis_showscale=False)
    # fig.update_layout(height=900)  # Ajusta la altura del mapa aquí
    return fig