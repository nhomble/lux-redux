from flask import request
import functools

import lux.services.chat_service as chat
import lux.services.info_service as info
from lux import lux, LUX_PORT, LUX_HOST, LUX_AUTH
from lux.services import VOID_RESPONSE
from lux.services.clients import GROUPME_BOT
from lux.transfer.inbound import GroupMeMessage


def authenticated(func):
    '''
    Poor mans auth since I haven't seen how groupme is going to do it nicely for us. People must provide the API key
    configured at start up
    :param func:
    :return:
    '''
    @functools.wraps(func)
    def wrapper(*args, **kwds):
        if lux.got_first_request and LUX_AUTH == request.args["TOKEN"]:
            return func(*args, **kwds)
        else:
            return VOID_RESPONSE, 403

    return wrapper


@lux.route('/api/v1', methods=['GET'])
def root():
    lux.logger.info("ping")
    return "ping"


@lux.route('/api/v1/info/about', methods=['GET'])
@authenticated
def about():
    '''
    Tell me about the app
    :return:
    '''
    lux.logger.info("Getting about")
    response = info.info_about()
    return response, 200


@lux.route('/api/v1/info/health', methods=['GET'])
@authenticated
def health_check():
    '''
    Tell me the health status
    :return:
    '''
    lux.logger.info("Getting health")
    response = info.info_health()
    return response, 200


@lux.route('/api/v1/chat/message/groupme', methods=['POST'])
@authenticated
def groupme_message():
    '''
    Handle a new groupme message
    '''
    message = GroupMeMessage.from_json(request.data)
    print(request.headers)
    if message.author == GROUPME_BOT.name:
        response = VOID_RESPONSE
    else:
        response = chat.groupme_message(message)

    return response, 200


if __name__ == "__main__":
    '''
    Now we have the option to start manually outside of
    $ flask
    
    **NOTE** this must be called after the routes are registered above
    '''
    print("Going to bind to HOST=" + LUX_HOST)
    print("Going to bind to PORT=" + LUX_PORT)
    lux.run(host=LUX_HOST, port=LUX_PORT)
