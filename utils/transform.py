'''Подготовка ответа hh для БД.'''


def prepare_json(vacancy):
    '''_summary_

    :param _type_ vacancy: _description_
    :return _type_: _description_
    '''
    if vacancy['salary'] is not None:
        salary_from = vacancy['salary']['from']
        salary_to = vacancy['salary']['to']
    else:
        salary_from = None
        salary_to = None
    return {
        'id': vacancy['id'],
        'url': vacancy['url'],
        'name': vacancy['name'],
        'area_name': vacancy['area']['name'],
        'employer_name': vacancy['employer']['name'],
        'schedule_name': vacancy['schedule']['name'],
        'published_at': vacancy['published_at'],
        'salary_from': salary_from,
        'salary_to': salary_to,
        'requirement': vacancy['snippet']['requirement'],
        'responsibility': vacancy['snippet']['responsibility']
    }
