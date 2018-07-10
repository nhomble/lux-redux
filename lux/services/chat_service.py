from lux.domain import ChatMessage
from lux.services import VOID_RESPONSE, GROUPME

from lux.services.bot import respond_to_chat
from lux.transfer.inbound import GroupMeMessage


def groupme_message(msg: GroupMeMessage):
    '''
    Handle incoming groupme message
    :return:
    '''
    message = ChatMessage(
        msg.author,
        msg.text,
        "GroupMe"
    )
    decision = respond_to_chat(message)
    if decision.should_respond:
        GROUPME.post(decision.reply)
    return VOID_RESPONSE
