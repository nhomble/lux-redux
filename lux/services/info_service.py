from lux.domain import About, Health
from lux.services import to_json


def info_about():
    '''
    Give a short summary of what
    :return:
    '''
    return to_json(About())


def info_health() -> dict:
    '''
    Tell me the health of the services
    :return:
    '''
    return to_json(Health())
