import os

import groupy
import jsonpickle

VOID_RESPONSE = ''
GROUPME_TOKEN_V = 'GROUPME_TOKEN'
GROUPME_NAME_V = 'GROUPME_NAME'

GROUPME_TOKEN = os.environ.get(GROUPME_TOKEN_V, None)
GROUPME_CLIENT = groupy.Client.from_token(GROUPME_TOKEN)
GROUPME_TARGET_GROUP = os.environ.get(GROUPME_NAME_V, None)

group = None
# a glorified first()
for g in GROUPME_CLIENT.groups.list():
    if g.name == GROUPME_TARGET_GROUP:
        group = g
        break

GROUPME = group
def to_json(obj):
    '''
    Wrap the jsonify function for all services here
    :param obj:
    :return:
    '''
    # unpicklable to avoid unwanted keys
    return jsonpickle.encode(obj, unpicklable=False)

