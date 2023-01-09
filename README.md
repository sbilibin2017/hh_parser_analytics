# ПРОЕКТ ПО АНАЛИЗУ ВАКАНСИЙ HH.RU

### элементы:
1. анализ спецификации API
2. проектирование БД
3. написание парсеров, регулярно поплняющих БД
4. аналитика
---

## 1. анализ спецификации API

ответ https://api.hh.ru/areas:

```
{'id': '1622', 'name': 'Звенигово'}
```


ответ https://api.hh.ru/vacancies:
```
{'accept_temporary': False,
 'address': {'building': '2Б',
             'city': 'Волжск',
             'description': None,
             'id': '6793413',
             'lat': 55.883499,
             'lng': 48.376021,
             'metro': None,
             'metro_stations': [],
             'raw': 'Волжск, улица 107-й Бригады, 2Б',
             'street': 'улица 107-й Бригады'},
 'adv_response_url': 'https://api.hh.ru/vacancies/73904523/adv_response?host=hh.ru',
 'alternate_url': 'https://hh.ru/vacancy/73904523',
 'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=73904523',
 'archived': False,
 'area': {'id': '1621',
          'name': 'Волжск',
          'url': 'https://api.hh.ru/areas/1621'},
 'contacts': None,
 'created_at': '2022-12-26T11:44:46+0300',
 'department': {'id': 'fixprice-196621-fixp', 'name': 'Fix Price'},
 'employer': {'alternate_url': 'https://hh.ru/employer/196621',
              'id': '196621',
              'logo_urls': {'240': 'https://hhcdn.ru/employer-logo/3425638.jpeg',
                            '90': 'https://hhcdn.ru/employer-logo/3425637.jpeg',
                            'original': 'https://hhcdn.ru/employer-logo-original/746169.jpg'},
              'name': 'FIX PRICE',
              'trusted': True,
              'url': 'https://api.hh.ru/employers/196621',
              'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=196621'},
 'has_test': False,
 'id': '73904523',
 'insider_interview': None,
 'name': 'Кассир в г. Волжск',
 'premium': False,
 'published_at': '2022-12-26T11:44:46+0300',
 'relations': [],
 'response_letter_required': False,
 'response_url': None,
 'salary': {'currency': 'RUR', 'from': 29000, 'gross': True, 'to': 32000},
 'schedule': {'id': 'shift', 'name': 'Сменный график'},
 'snippet': {'requirement': 'Наши преимущества: - Мы рады кандидатам как с '
                            'опытом работы, так и новичкам.',
             'responsibility': 'Работа с кассой, кассовые операции. - Выкладка '
                               'товара по планограмме. - Контроль порядка в '
                               'торговом зале и сроков годности товара.'},
 'sort_point_distance': None,
 'type': {'id': 'open', 'name': 'Открытая'},
 'url': 'https://api.hh.ru/vacancies/73904523?host=hh.ru',
 'working_days': [],
 'working_time_intervals': [],
 'working_time_modes': []}
```

### 2. проектирование БД
Используется одна таблица ```Vacancies```

```
CREATE TABLE vacancies(
    id integer PRIMARY KEY,
    url text,
    name varchar(256),
    area_name varchar(256),
    published_at timestamp with time zone,
    employer_name varchar(256),
    schedule_name varchar(256),
    salary_from varchar(256),
    salary_to varchar(256),
    requirement text,
    responsibility text
);
```
БД поднимается в докер контейнере, для аохранения данных используется ```volume```

### 3. написание парсеров, регулярно поплняющих БД

    *  архитектура парсера

```
├── database
│   ├── docker-compose.yaml
│   └── init.sql
├── env.example
├── __init__.py
├── openapi.yml
├── parser│   
│   ├── etl.log
│   ├── __init__.py
│   ├── main.py
│   ├── __pycache__
│   │   ├── __init__.cpython-310.pyc
│   │   └── src.cpython-310.pyc
│   ├── requirements-dev.txt
│   ├── requirements.txt
|   ├── venv
│   
├── __pycache__
│   └── __init__.cpython-310.pyc
├── README.md
└── utils
    ├── constants.py
    ├── extract.py
    ├── load.py
    ├── logger.py
    ├── __pycache__
    │   ├── constants.cpython-310.pyc
    │   ├── extract.cpython-310.pyc
    │   ├── load.cpython-310.pyc
    │   ├── logger.cpython-310.pyc
    │   ├── transform.cpython-310.pyc
    │   └── validators.cpython-310.pyc
    ├── transform.py
    └── validators.py

    

```



