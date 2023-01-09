'''Заполнение БД.'''

import os
from contextlib import closing
from pathlib import Path
from typing import Tuple

import psycopg2
from dotenv import load_dotenv

from hh_parser_analytics.utils.constants import TABLE_COLNAMES

p = Path(__file__).parents[1] / '.env.dev'

load_dotenv(p)


def get_query_with_values(values: tuple) -> Tuple[str, tuple]:
    '''_summary_

    :param _type_ values: _description_
    '''
    colnames_str = ','.join(TABLE_COLNAMES)
    placeholder = ','.join(['%s' for _ in range(len(TABLE_COLNAMES))])
    values_to_insert = tuple([values[k] for k in TABLE_COLNAMES])

    postgres_insert_query = f""" INSERT INTO content.vacancies \
                ({colnames_str}) VALUES ({placeholder})"""

    return postgres_insert_query, values_to_insert


def execute_query(query: str, values: tuple) -> None:
    '''_summary_

    :param _type_ query: _description_
    :param _type_ values: _description_
    '''
    with closing(psycopg2.connect(
            user=os.getenv('POSTGRES_USER'),
            password=os.getenv('POSTGRES_PASSWORD'),
            host="127.0.0.1",
            port="5432",
            database=os.getenv('POSTGRES_DB'))
    ) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, values)
            conn.commit()
