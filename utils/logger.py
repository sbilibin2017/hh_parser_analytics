'''Логгер для мониторинга.'''
import logging

logging.basicConfig(
    filename='etl.log',
    format='[%(levelname)s]: %(message)s',
    level=logging.DEBUG,
    filemode='w'
)
logger = logging.getLogger('etl')
