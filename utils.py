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
    {'label': 'Lesiones leves', 'value': 'lesiones_leves'},
    {'label': 'Lesiones menos graves, graves o gravísimas', 'value': 'lesiones_graves'},
    {'label': 'Otros robos con fuerza', 'value': 'otros_robos_fuerza'},
    {'label': 'Robo con violencia o intimidación', 'value': 'robo_violencia'},
    {'label': 'Robo de objetos de o desde vehículo', 'value': 'robo_objetos_vehiculo'},
    {'label': 'Robo de vehículo motorizado', 'value': 'robo_vehiculo'},
    {'label': 'Robo en lugar habitado', 'value': 'robo_lugar_habitado'},
    {'label': 'Robo en lugar no habitado', 'value': 'robo_lugar_no_habitado'},
    {'label': 'Robo por sorpresa', 'value': 'robo_sorpresa'},
    {'label': 'Violaciones', 'value': 'violaciones'},
    {'label': 'Abandono de armas', 'value': 'abandono_armas'},
    {'label': 'Hallazgo de armas o explosivos', 'value': 'hallazgo_armas_explosivos'},
    {'label': 'Otros ley de armas', 'value': 'otros_ley_armas'},
    {'label': 'Porte de armas', 'value': 'porte_armas'},
    {'label': 'Tenencia ilegal de armas o explosivos', 'value': 'tenencia_ilegal_armas_explosivos'},
    {'label': 'Amenazas', 'value': 'amenazas'},
    {'label': 'Comercio ambulante o clandestino', 'value': 'comercio_ambulante_clandestino'},
    {'label': 'Consumo alcohol vía pública', 'value': 'consumo_alcohol_via_publica'},
    {'label': 'Daños', 'value': 'danios'},
    {'label': 'Desórdenes', 'value': 'desordenes'},
    {'label': 'Ebriedad', 'value': 'ebriedad'},
    {'label': 'Otras incivilidades', 'value': 'otras_incivilidades'},
    {'label': 'Riña pública', 'value': 'rina_publica'},
    {'label': 'Ruidos molestos', 'value': 'ruidos_molestos'},
    {'label': 'Violencia intrafamiliar a adulto mayor', 'value': 'violencia_intrafamiliar_adulto_mayor'},
    {'label': 'Violencia intrafamiliar a hombre', 'value': 'violencia_intrafamiliar_hombre'},
    {'label': 'Violencia intrafamiliar a mujer', 'value': 'violencia_intrafamiliar_mujer'},
    {'label': 'Violencia intrafamiliar a niño', 'value': 'violencia_intrafamiliar_nino'},
    {'label': 'Violencia intrafamiliar no clasificado', 'value': 'violencia_intrafamiliar_no_clasificado'},
    {'label': 'Receptación', 'value': 'receptacion'},
    {'label': 'Robo frustrado', 'value': 'robo_frustrado'}
]

OPCIONES_TERRITORIO = [
    # {'label': 'Nacional', 'value': 'Nacional'},
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