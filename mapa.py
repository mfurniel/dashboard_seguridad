import pandas as pd
import requests
import plotly.express as px
import utils as nConst
def mapChile():
    regions = ['Región de Arica y Parinacota', 'Región de Tarapacá', 'Región de Antofagasta', 'Región de Magallanes y Antártica Chilena',
            'Región de Aysén del Gral.Ibañez del Campo', 'Región de Atacama', "Región de Coquimbo", 'Región de Valparaíso',
            'Región Metropolitana de Santiago', 'Región de Los Lagos', 'Región de Los Ríos', 'Región de La Araucanía', 'Región del Bío-Bío', 
            'Región de Ñuble', 'Región del Maule', 'Región del Libertador Bernardo O\'Higgins']

    # Como ejemplo, creamos un dataframe con los nombres descritos en regions, llenando los campos de la columna NAME_REG
    df = pd.DataFrame(regions, columns=['NAME_REG'])

    # Para demostración, creamos una columna con la longitud del nombre de la región
    df['name_length'] = df['NAME_REG'].str.len()
    tarapaca = pd.read_excel(nConst.EXCEL_PATH[1])
    antofa = pd.read_excel(nConst.EXCEL_PATH[2])
    ataca = pd.read_excel(nConst.EXCEL_PATH[3])
    coqui = pd.read_excel(nConst.EXCEL_PATH[4])
    valpa = pd.read_excel(nConst.EXCEL_PATH[5])
    ohig = pd.read_excel(nConst.EXCEL_PATH[6])
    maule = pd.read_excel(nConst.EXCEL_PATH[7])
    bio = pd.read_excel(nConst.EXCEL_PATH[8])
    arau = pd.read_excel(nConst.EXCEL_PATH[9])
    lagos = pd.read_excel(nConst.EXCEL_PATH[10])
    aysen = pd.read_excel(nConst.EXCEL_PATH[11])
    maga = pd.read_excel(nConst.EXCEL_PATH[12])
    metro = pd.read_excel(nConst.EXCEL_PATH[13])
    rios = pd.read_excel(nConst.EXCEL_PATH[14])
    arica = pd.read_excel(nConst.EXCEL_PATH[15])
    nyuble = pd.read_excel(nConst.EXCEL_PATH[16])
    
    tarapaca['Total'] = tarapaca.select_dtypes(include='number').sum(axis=1)
    tarasum = tarapaca['Total'].sum()

    antofa['Total'] = antofa.select_dtypes(include='number').sum(axis=1)
    antofasum = antofa['Total'].sum()

    ataca['Total'] = ataca.select_dtypes(include='number').sum(axis=1)
    atacasum = ataca['Total'].sum()

    coqui['Total'] = coqui.select_dtypes(include='number').sum(axis=1)
    coquisum = coqui['Total'].sum()

    valpa['Total'] = valpa.select_dtypes(include='number').sum(axis=1)
    valpasum = valpa['Total'].sum()

    ohig['Total'] = ohig.select_dtypes(include='number').sum(axis=1)
    ohigsum = ohig['Total'].sum()

    maule['Total'] = maule.select_dtypes(include='number').sum(axis=1)
    maulesum = maule['Total'].sum()

    bio['Total'] = bio.select_dtypes(include='number').sum(axis=1)
    biosum = bio['Total'].sum()
    
    arau['Total'] = arau.select_dtypes(include='number').sum(axis=1)
    arausum = arau['Total'].sum()

    lagos['Total'] = lagos.select_dtypes(include='number').sum(axis=1)
    lagossum = lagos['Total'].sum()

    aysen['Total'] = aysen.select_dtypes(include='number').sum(axis=1)
    aysensum = aysen['Total'].sum()

    maga['Total'] = maga.select_dtypes(include='number').sum(axis=1)
    magasum = maga['Total'].sum()

    metro['Total'] = metro.select_dtypes(include='number').sum(axis=1)
    metrosum = metro['Total'].sum()

    rios['Total'] = rios.select_dtypes(include='number').sum(axis=1)
    riossum = rios['Total'].sum()

    arica['Total'] = arica.select_dtypes(include='number').sum(axis=1)
    aricasum = arica['Total'].sum()

    nyuble['Total'] = nyuble.select_dtypes(include='number').sum(axis=1)
    nyublesum = nyuble['Total'].sum()

    df['Cantidad'] = [aricasum, tarasum, antofasum, magasum, aysensum, atacasum, coquisum, valpasum, metrosum, lagossum, riossum, arausum, biosum, nyublesum, maulesum, ohigsum]

    # Leemos los datos del GeoJSON de los límites regionales de Chile desde GitHub
    repo_url = 'https://raw.githubusercontent.com/caracena/chile-geojson/master/regiones.json'
    chile_regions_geo = requests.get(repo_url).json()

    # Coroplético que representa la longitud de los nombres de las regiones de Chile
    fig = px.choropleth(data_frame=df,
                        geojson=chile_regions_geo, 
                        locations='NAME_REG', # nombre de la columna relevante del dataframe
                        featureidkey='properties.Region',  # ruta del campo del feature de GeoJSON con cuyos valores se cotejan los valores de la columna relevante
                        color='Cantidad',
                        color_continuous_scale="YlOrRd",
                        range_color=(0, df['Cantidad'].max()),
                        scope="south america",
                    )
    fig.update_geos(showcountries=False, showcoastlines=False, showland=False, fitbounds="locations")
    # fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.update_layout(
        # autosize=False, 
        # margin=dict(l=0, r=0, t=0, b=0),  # Ajusta los márgenes del gráfico
        height=500,  # Establece la altura del gráfico en píxeles
        width=335,
        title_text="Mapa de delitos total en Chile 2005-2022",
        title_font_size=14,
    )
    fig.update_layout(coloraxis_showscale=True)
    # fig.update_layout(height=900)  # Ajusta la altura del mapa aquí
    return fig