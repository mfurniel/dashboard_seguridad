#Definimos Constantes
GRUPOS_DELITOS=[
    'Delitos de mayor connotación social',
    'Infracción a ley de armas',
    'Incivilidades'
    'Abigeato',
    'Abusos sexuales y otros delitos sexuales',
    'Violencia intrafamiliar',
    'Receptación',
    'Robo frustrado',
]



DELITOS = {
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