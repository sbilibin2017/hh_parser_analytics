'''Константы.'''

URL_AREAS = 'https://api.hh.ru/areas'
URL_VACANCIES = 'https://api.hh.ru/vacancies'
PER_PAGE = 100
TIMEOUT = 5
TABLE_COLNAMES = (
    'id', 'url', 'name', 'area_name', 'employer_name', 'schedule_name',
    'published_at', 'salary_from', 'salary_to', 'requirement', 'responsibility'
)
WAIT_TIME = 60 * 60
