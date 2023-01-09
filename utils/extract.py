'''Получение ответа от  hh api.'''

import json
import time
from collections import OrderedDict
from typing import Tuple

import requests

from hh_parser_analytics.utils.constants import (PER_PAGE, TIMEOUT, URL_AREAS,
                                                 URL_VACANCIES, WAIT_TIME)
from hh_parser_analytics.utils.logger import logger


def get_all_areas():
    '''_summary_

    :return _type_: _description_
    '''
    logger.info('Starting ...')
    request = requests.get(URL_AREAS, timeout=TIMEOUT)
    status_code = request.status_code
    if status_code == 200:
        items = json.loads(request.content.decode())
        logger.info('> items count = %d', len(items))
        d_areas = {}
        for i, item in enumerate(items):
            logger.info('\t> item#%d', i + 1)
            for j, area_outer in enumerate(item['areas']):
                d_areas[int(area_outer['id'])] = area_outer['name']
                logger.info('\t> %d. area outer: %s',
                            j + 1, area_outer['name'])
                for k, area_inner in enumerate(area_outer['areas']):
                    d_areas[int(area_inner['id'])] = area_inner['name']
                    logger.info('\t\t> %d.%d. area inner: %s',
                                j + 1, k + 1, area_inner['name'])
        d_areas = OrderedDict(sorted(d_areas.items()))
        logger.info('> areas %s', d_areas)
        logger.info(
            '-------------------------------------------------------------------------------------')
        return d_areas
    else:
        logger.info('\t\t> status code -> %d', request.status_code)
        return None


def get_request(area_id: int, page: int) -> Tuple[dict, int]:
    '''_summary_

    :yield _type_: _description_
    '''
    params = {'area': area_id, 'page': page, 'per_page': PER_PAGE}
    logger.info('\t> page -> %s', page)
    request = requests.get(URL_VACANCIES, params, timeout=TIMEOUT)
    content = json.loads(request.content.decode())
    logger.info('\t\t> status code -> %d', request.status_code)
    status_code = int(request.status_code)
    return content, status_code


def get_vacancies(d_areas: dict) -> dict:
    '''_summary_

    :return _type_: _description_
    '''
    if d_areas is not None:
        for i, (area_id, area_name) in enumerate(d_areas.items()):
            logger.info('> %d. area ->: %s(%s)', i + 1, area_name, area_id)
            page = 1
            while True:
                content, status_code = get_request(area_id, page)
                if status_code == 200:
                    items = content['items']
                    if len(items) == 0:
                        logger.info('\t\t> items count -> %d', len(items))
                        break
                    logger.info('\t\t> items count -> %d', len(items))
                    for item in items:
                        yield item
                    page += 1
                else:
                    break
            if status_code == 403:
                logger.info('> WATING FOR 1 HOUR ...')
                time.sleep(WAIT_TIME)
