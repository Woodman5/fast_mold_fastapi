import pycountry

standard_type_list = [
        'iso',
        'gost',
        'din',
        'astm',
        'brookfield lvt',
    ]

application_type_list = [
    'temperature',
    'density',
    'strength',
    'viscosity',
    'electricity',
    'shrinkage',
    'moisture absorption',
    'hardness',
    'flammability',
    'lifetime',
]

color_type_list = [
        'regular colors',
        'ral',
    ]

countries = [x.alpha_2 for x in pycountry.countries]

