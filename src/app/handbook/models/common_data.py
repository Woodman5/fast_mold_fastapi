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
    None
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
    None
)

fiber_type_list = (
    'Стекловолокно',
    'Арамид',
    'Углеволокно',
    None
)

netting_list = (
    'UD',
    'Plane',
    'Twill',
    '3H',
    '8H',
    None
)

core_type_list = [
    'Коремат',
    'Пенопласт',
    'Соты',
    None
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
    None
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
    None
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

application_choices = [
    ('Aircraft and Aerospace', (
        ('cd1', 'Cocpit doors'),
        ('ct1', 'Cryogenic tanks'),
        ('gal', 'Galleys'),
        ('gc1', 'Galley carts'),
        ('ga1', 'General aviation (fuselage and wing)'),
        ('hrb', 'Helicopter rotor blades'),
        ('ip1', 'Insulating panels'),
        ('in1', 'Interiors'),
        ('mt1', 'Meal trolleys'),
        ('rad', 'Radomes'),
    )
     ),
    ('Defense', (
        ('ant', 'Antennas'),
        ('ccs', 'Combat communication systems'),
        ('ns2', 'Naval superstructures'),
    )
     ),
    ('Road and Rail', (
        ('cb3', 'Car bodies'),
        ('co3', 'Covers'),
        ('def', 'Deflectors'),
        ('do3', 'Doors'),
        ('ec3', 'Engine covers'),
        ('fl3', 'Floors'),
        ('fe3', 'Front ends'),
        ('hl3', 'Headliners'),
        ('in3', 'Interiors'),
        ('ip3', 'Interior panels'),
        ('pw3', 'Partition walls'),
        ('rf3', 'Roofs'),
        ('rp3', 'Roof panels'),
        ('se3', 'Seats'),
        ('ss3', 'Side skirts'),
        ('sw3', 'Sidewalls'),
        ('spo', 'Spoilers'),
        ('tp3', 'Truck panels'),
    )
     ),
    ('Automotive', (
        ('co4', 'Covers'),
        ('fl4', 'Floors'),
        ('in4', 'Interior'),
        ('sw4', 'Sidewalls'),
        ('sp4', 'Structural parts'),
        ('tbp', 'Truck body parts'),
    )
     ),
    ('Wind energy', (
        ('bl5', 'Blades (shear webs & shells)'),
        ('bh5', 'Bulkheads'),
        ('eb5', 'Engine beds'),
        ('fl5', 'Floors'),
        ('in5', 'Interiors'),
        ('lr5', 'Local reinforcements'),
        ('na5', 'Nacelles'),
        ('rb5', 'Rotor blades'),
        ('so5', 'Soles'),
        ('st5', 'Stringers'),
        ('tm5', 'Tooling and molds'),
        ('tr5', 'Transoms'),
        ('tgh', 'Turbine generator housings'),
    )
     ),
    ('Marine', (
        ('bh6', 'Bulkheads'),
        ('de6', 'Decks'),
        ('eb6', 'Engine beds'),
        ('eh6', 'Engine hatches'),
        ('ff6', 'Fast-ferries'),
        ('fri', 'Fire resistant interiors'),
        ('fl6', 'Floors'),
        ('hu6', 'Hulls'),
        ('hs6', 'Hull sides'),
        ('in6', 'Interiors'),
        ('lr6', 'Local reinforcements'),
        ('ra6', 'Radomes'),
        ('st6', 'Stringers'),
        ('ss6', 'Superstructures'),
        ('tm6', 'Tooling and molds'),
        ('tr6', 'Transoms'),
    )
     ),
    ('Recreation', (
        ('ca7', 'Canoes'),
        ('ka7', 'Kayaks'),
        ('sk7', 'Skis'),
        ('sb7', 'Snowboards'),
        ('su7', 'Surfboards'),
        ('wb7', 'Wakeboards'),
    )
     ),
    ('Industrial', (
        ('ap8', 'Architectural panels'),
        ('cpf', 'Concrete pouring forms'),
        ('cn8', 'Containers'),
        ('co8', 'Covers'),
        ('dw8', 'Ductwork'),
        ('fl8', 'Floors'),
        ('htt', 'High temperature tooling'),
        ('lr8', 'Local reinforcements'),
        ('ra8', 'Radomes'),
        ('sh8', 'Shelters'),
        ('sg8', 'Sporting goods'),
        ('ta8', 'Tanks'),
        ('to8', 'Tooling'),
        ('tm8', 'Tooling and molds'),
        ('tse', 'Tub and shower enclosures'),
        ('xr8', 'X-ray tables'),
    )
     ),
    ('Consumer', (
        ('med', 'Medical'),
        ('phr', 'Pharmaceutical'),
        ('fod', 'Food'),
    )
     ),
]
