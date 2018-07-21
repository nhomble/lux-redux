from flask import request

import lux.services.chat_service as chat
import lux.services.info_service as info
from lux import lux, LUX_PORT
from lux.transfer.inbound import GroupMeMessage


@lux.route('/api/v1', methods=['GET'])
def root():
    lux.logger.info("ping")
    return "ping"


@lux.route('/api/v1/info/about', methods=['GET'])
def about():
    '''
    Tell me about the app
    :return:
    '''
    lux.logger.info("Getting about")
    response = info.info_about()
    return response, 200


@lux.route('/api/v1/info/health', methods=['GET'])
def health_check():
    '''
    Tell me the health status
    :return:
    '''
    lux.logger.info("Getting health")
    response = info.info_health()
    return response, 200


@lux.route('/api/v1/chat/message/groupme', methods=['POST'])
def groupme_message():
    '''
    Handle a new groupme message
    '''
    message = GroupMeMessage.from_json(request.data)
    lux.logger.info("Handling groupme message " + str(message))
    response = chat.groupme_message(message)
    return response, 200


if __name__ == "__main__":
    '''
    Now we have the option to start manually outside of
    $ flask
    
    **NOTE** this must be called after the routes are registered above
    '''
    print("Going to bind to PORT=" + LUX_PORT)
    lux.run(port=LUX_PORT)
