'''Коллекционирование регионов.'''

from dataclasses import asdict
from pathlib import Path

from dotenv import load_dotenv

from hh_parser_analytics.utils import extract, load, transform, validators
from hh_parser_analytics.utils.logger import logger

p = Path(__file__).parents[1] / '.env.dev'

load_dotenv(p)


def main() -> None:
    '''точка входа'''
    all_areas = extract.get_all_areas()
    for vacancy in extract.get_vacancies(all_areas):
        vacancy_prepared = transform.prepare_json(vacancy)
        logger.info('\t\t> preparing json')
        vacancy_validated = asdict(
            validators.Vacancy(**vacancy_prepared))
        logger.info('\t\t> validating json')
        query, values = load.get_query_with_values(vacancy_validated)
        logger.info('\t\t> query, values')
        try:
            load.execute_query(query, values)
            logger.info('\t\t\t> new data:\n\t\t\t%s', str(values))
            logger.info(
                '\t\t--------------------------------------------------')
        except:
            logger.info('\t\t\t> already in db:\n\t\t\t%s', str(values))
            logger.info(
                '\t\t--------------------------------------------------')


if __name__ == '__main__':
    main()
