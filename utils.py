#Definimos Constantes
GRUPOS_DELITOS=[
    'Delitos de mayor connotación social',
    'Infracción a ley de armas',
    'Incivilidades',
    'Abigeato',
    'Abusos sexuales y otros delitos sexuales',
    'Violencia intrafamiliar',
    'Receptación',
    'Robo frustrado',
]



DELITOS_CON_GRUPOS = {
        'Delitos de mayor connotación social': [
            'Homicidios',
            'Hurtos',
            'Lesiones leves',
            'Lesiones menos graves, graves o gravísimas',
            'Otros robos con fuerza',
            'Robo con violencia o intimidación',
            'Robo de objetos de o desde vehículo',
            'Robo de vehículo motorizado',
            'Robo en lugar habitado',
            'Robo en lugar no habitado',
            'Robo por sorpresa',
            'Violaciones',
        ],
        'Infracción a ley de armas': [
            'Abandono de armas',
            'Hallazgo de armas o explosivos',
            'Otros ley de armas',
            'Porte de armas',
            'Tenencia ilegal de armas o explosivos',
        ],
        'Incivilidades': [
            'Amenazas',
            'Comercio ambulante o clandestino',
            'Consumo alcohol vía pública',
            'Daños',
            'Desórdenes',
            'Ebriedad',
            'Otras incivilidades',
            'Riña pública',
            'Ruidos molestos',
        ],
        'Abigeato': [],
        'Abusos sexuales y otros delitos sexuales': [],
        'Violencia intrafamiliar': [
            'Violencia intrafamiliar a adulto mayor',
            'Violencia intrafamiliar a hombre',
            'Violencia intrafamiliar a mujer',
            'Violencia intrafamiliar a niño',
            'Violencia intrafamiliar no clasificado',
        ],
        'Receptación': [],
        'Robo frustrado': [],
    }

DELITOS = [
    'Homicidios',
    'Hurtos',
    'Lesiones leves',
    'Lesiones menos graves, graves o gravísimas',
    'Otros robos con fuerza',
    'Robo con violencia o intimidación',
    'Robo de objetos de o desde vehículo',
    'Robo de vehículo motorizado',
    'Robo en lugar habitado',
    'Robo en lugar no habitado',
    'Robo por sorpresa',
    'Violaciones',
    'Abandono de armas',
    'Hallazgo de armas o explosivos',
    'Otros ley de armas',
    'Porte de armas',
    'Tenencia ilegal de armas o explosivos',
    'Amenazas',
    'Comercio ambulante o clandestino',
    'Consumo alcohol vía pública',
    'Daños',
    'Desórdenes',
    'Ebriedad',
    'Otras incivilidades',
    'Riña pública',
    'Ruidos molestos',
    'Violencia intrafamiliar a adulto mayor',
    'Violencia intrafamiliar a hombre',
    'Violencia intrafamiliar a mujer',
    'Violencia intrafamiliar a niño',
    'Violencia intrafamiliar no clasificado',
    'Receptación',
    'Robo frustrado'
]


SUBCATEGORIAS =[
    'casospoliciales',
    'denuncias',
    'detenciones',
    'aprehendidos',
]

EXCEL_PATH = [
    'dataset/nacional/nacional_por_anyos.xlsx',     # 0
    'dataset/region/tarapaca_por_anyos.xlsx',       # 1
    'dataset/region/antofagasta_por_anyos.xlsx',    # 2
    'dataset/region/atacama_por_anyos.xlsx',        # 3
    'dataset/region/coquimbo_por_anyos.xlsx',       # 4
    'dataset/region/valparaiso_por_anyos.xlsx',     # 5
    'dataset/region/ohiggins_por_anyos.xlsx',       # 6
    'dataset/region/maule_por_anyos.xlsx',          # 7
    'dataset/region/biobio_por_anyos.xlsx',         # 8
    'dataset/region/araucania_por_anyos.xlsx',      # 9
    'dataset/region/lagos_por_anyo.xlsx',           # 10
    'dataset/region/aysen_por_anyos.xlsx',          # 11
    'dataset/region/magallanes_por_anyos.xlsx',     # 12
    'dataset/region/metropolitana_por_anyos.xlsx',  # 13
    'dataset/region/rios_por_anyos.xlsx',           # 14
    'dataset/region/arica_por_anyos.xlsx',          # 15
    'dataset/region/nyuble_por_anyos.xlsx',         # 16
]

EXCEL_PATH_SE = [
    'dataset/nacional/sexo_edad_nacional.xlsx',   # 0
    'dataset/region/sexo_edad_tarapaca.xlsx',     # 1
    'dataset/region/sexo_edad_antofagasta.xlsx',  # 2
    'dataset/region/sexo_edad_atacama.xlsx',      # 3
    'dataset/region/sexo_edad_coquimbo.xlsx',     # 4
    'dataset/region/sexo_edad_valparaiso.xlsx',   # 5
    'dataset/region/sexo_edad_ohiggins.xlsx',     # 6
    'dataset/region/sexo_edad_maule.xlsx',        # 7
    'dataset/region/sexo_edad_biobio.xlsx',       # 8
    'dataset/region/sexo_edad_araucania.xlsx',    # 9
    'dataset/region/sexo_edad_lagos.xlsx',        # 10
    'dataset/region/sexo_edad_aysen.xlsx',        # 11
    'dataset/region/sexo_edad_magallanes.xlsx',   # 12
    'dataset/region/sexo_edad_metropolitana.xlsx',# 13
    'dataset/region/sexo_edad_rios.xlsx',         # 14
    'dataset/region/sexo_edad_arica.xlsx',        # 15
    'dataset/region/sexo_edad_nyuble.xlsx',       # 16
]

TERRITORIO = [
    'Chile',                            # 0
    'Región de Tarapacá',               # 1
    'Región de Antofagasta',            # 2
    'Región de Atacama',                # 3
    'Región de Coquimbo',               # 4
    'Región de Valparaíso',             # 5
    "Región de O'Higgins",              # 6
    'Región del Maule',                 # 7
    'Región del Biobío',                # 8
    'Región de La Araucanía',           # 9
    'Región de Los Lagos',              # 10
    'Región de Aysén',                  # 11
    'Región de Magallanes',             # 12
    'Región Metropolitana',             # 13
    'Región de Los Ríos',               # 14
    'Región de Arica y Parinacota',     # 15
    'Región de Ñuble',                  # 16
]


# print(DELITOS[GRUPOS_DELITOS[0]][0]) #output homicidios

OPCIONES_DELITOS = [
    {'label': 'Delitos de mayor connotación social','value': 'delitos de mayor connotación social'},
    {'label':'Infracción a ley de armas','value': 'infracción a ley de armas'},
    {'label':'Incivilidades','value': 'incivilidades'},
    {'label':'Abigeato','value': 'abigeato'},
    {'label':'Abusos sexuales y otros delitos sexuales','value': 'abusos sexuales y otros delitos sexuales'},
    {'label':'Violencia intrafamiliar','value': 'violencia intrafamiliar'},
    {'label':'Receptación','value': 'receptación'},
    {'label':'Robo frustrado','value': 'robo frustrado'},
    {'label': 'Homicidios', 'value': 'homicidios'},
    {'label': 'Hurtos', 'value': 'hurtos'},
    {'label': 'Lesiones leves', 'value': 'lesiones leves'},
    {'label': 'Lesiones menos graves, graves o gravísimas', 'value': 'lesiones menos graves, graves o gravísimas'},
    {'label': 'Otros robos con fuerza', 'value': 'otros robos con fuerza'},
    {'label': 'Robo con violencia o intimidación', 'value': 'robo con violencia o intimidación'},
    {'label': 'Robo de objetos de o desde vehículo', 'value': 'robo de objetos de o desde vehículo'},
    {'label': 'Robo de vehículo motorizado', 'value': 'Robo de vehículo motorizado'},
    {'label': 'Robo en lugar habitado', 'value': 'robo en lugar habitado'},
    {'label': 'Robo en lugar no habitado', 'value': 'robo en lugar no habitado'},
    {'label': 'Robo por sorpresa', 'value': 'robo por sorpresa'},
    {'label': 'Violaciones', 'value': 'violaciones'},
    {'label': 'Abandono de armas', 'value': 'abandono de armas'},
    {'label': 'Hallazgo de armas o explosivos', 'value': 'Hallazgo de armas o explosivos'},
    {'label': 'Otros ley de armas', 'value': 'otros ley de armas'},
    {'label': 'Porte de armas', 'value': 'porte de armas'},
    {'label': 'Tenencia ilegal de armas o explosivos', 'value': 'Tenencia ilegal de armas o explosivos'},
    {'label': 'Amenazas', 'value': 'amenazas'},
    {'label': 'Comercio ambulante o clandestino', 'value': 'comercio ambulante o clandestino'},
    {'label': 'Consumo alcohol vía pública', 'value': 'consumo alcohol vía pública'},
    {'label': 'Daños', 'value': 'daños'},
    {'label': 'Desórdenes', 'value': 'desórdenes'},
    {'label': 'Ebriedad', 'value': 'ebriedad'},
    {'label': 'Otras incivilidades', 'value': 'otras incivilidades'},
    {'label': 'Riña pública', 'value': 'riña publica'},
    {'label': 'Ruidos molestos', 'value': 'ruidos molestos'},
    {'label': 'Violencia intrafamiliar a adulto mayor', 'value': 'violencia intrafamiliar a adulto mayor'},
    {'label': 'Violencia intrafamiliar a hombre', 'value': 'violencia intrafamiliar a hombre'},
    {'label': 'Violencia intrafamiliar a mujer', 'value': 'violencia intrafamiliar a mujer'},
    {'label': 'Violencia intrafamiliar a niño', 'value': 'violencia intrafamiliar a niño'},
    {'label': 'Violencia intrafamiliar no clasificado', 'value': 'violencia intrafamiliar no clasificado'},
    {'label': 'Receptación', 'value': 'receptacion'},
    {'label': 'Robo frustrado', 'value': 'robo frustrado'}
]

OPCIONES_TERRITORIO = [
    {'label': 'Nacional', 'value': '0'},
    {'label': 'Arica y Parinacota', 'value': '15'},
    {'label': 'Tarapacá', 'value': '2'},
    {'label': 'Atacama', 'value': '3'},
    {'label': 'Coquimbo', 'value': '4'},
    {'label': 'Valparaíso', 'value': '5'},
    {'label': 'Metropolitana', 'value': '13'},
    {'label': "O'Higgins", 'value': "6"},
    {'label': 'Maule', 'value': '7'},
    {'label': 'Ñuble', 'value': '16'},
    {'label': 'Biobío', 'value': '8'},
    {'label': 'Araucanía', 'value': '9'},
    {'label': 'Ríos', 'value': '14'},
    {'label': 'Lagos', 'value': '10'},
    {'label': 'Aysén', 'value': '11'},
    {'label': 'Magallanes', 'value': '12'},   
]

OPCIONES_ANYOS = [
    {'label': '2005', 'value': '2005'},
    {'label': '2006', 'value': '2006'},
    {'label': '2007', 'value': '2007'},
    {'label': '2008', 'value': '2008'},
    {'label': '2009', 'value': '2009'},
    {'label': '2010', 'value': '2010'},
    {'label': '2011', 'value': '2011'},
    {'label': '2012', 'value': '2012'},
    {'label': '2013', 'value': '2013'},
    {'label': '2014', 'value': '2014'},
    {'label': '2015', 'value': '2015'},
    {'label': '2016', 'value': '2016'},
    {'label': '2017', 'value': '2017'},
    {'label': '2018', 'value': '2018'},
    {'label': '2019', 'value': '2019'},
    {'label': '2020', 'value': '2020'},
    {'label': '2021', 'value': '2021'},
    {'label': '2022', 'value': '2022'}
]
