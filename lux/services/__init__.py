import jsonpickle

VOID_RESPONSE = ''


def to_json(obj):
    '''
    Wrap the jsonify function for all services here
    :param obj:
    :return:
    '''
    # unpicklable to avoid unwanted keys
    return jsonpickle.encode(obj, unpicklable=False)
