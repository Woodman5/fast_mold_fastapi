import pycountry

standard_type_list = (
        'iso',
        'gost',
        'din',
        'astm',
        'brookfield lvt',
    )

application_type_list = (
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
)

color_type_list = (
        'regular colors',
        'ral',
    )

countries = [x.alpha_2 for x in pycountry.countries]

flammability_list = (
    'Горючий',
    'Не поддерживающий горение',
    'Самозатухающий',
)

mat_type_list = (
        'Жидкость',
        'Нить',
        'Фракция',
    )

resin_type_list = (
    'Бесполиэмидное',
    'Винилэфирное',
    'Полиэмидное',
    'Полиэфирное',
    'Цианэфирное',
    'Эпоксивенилэфирное',
    'Эпоксидное',
)

fiber_form_list = (
    'Ровинг',
    'Ткань',
    'Стекломат',
)

fiber_type_list = (
    'Стекловолокно',
    'Арамид',
    'Углеволокно',
)

netting_list = (
    'UD',
    'Plane',
    'Twill',
    '3H',
    '8H',
)

core_type_list = [
    'Коремат',
    'Пенопласт',
    'Соты',
]
core_material_list = (
    'Алюминий',
    'Арамид',
    'Поливенилхлорид',
    'Полиметакрилимит',
    'Полистирол',
    'Полиуретан',
    'Стеклопластик',
    'Углепластик',
)
default_thickness_list = (
    '3',
    '5',
    '10',
    '15',
    '20',
    '25',
    '30',
    '40',
    '50',
    '60',
    '70',
    '80',
    '90',
    '100',
)

characteristic_type_list = (
    'Температура',
    'Плотность',
    'Прочность',
    'Вязкость',
    'Электричество',
    'Усадка',
    'Влагопоглощение',
    'Твердость',
    'Технология',
)
value_type_list = (
    'Короткий текст',
    'Длинный текст',
    'Ссылка',
    'Целое число',
    'Дробное число',
)

painting_list = (
        'Окраска в массе пигментами',
        'Окрашивание поверхности',
        'Окрашивание в оснастке',
    )
