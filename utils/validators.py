'''Валидаторы.'''


from datetime import datetime
from typing import Optional

from pydantic.dataclasses import dataclass


@dataclass
class Vacancy:
    '''_summary_'''
    id: int
    url: str
    name: str
    area_name: str
    published_at: datetime
    employer_name: Optional[str]
    schedule_name: Optional[str]
    salary_from: Optional[str]
    salary_to: Optional[str]
    requirement: Optional[str]
    responsibility: Optional[str]
