from lux.domain import ChatMessage
from lux.services.clients import GROUPME_BOT_NAME
import random


class ChatDecision():
    def __init__(self, respond=False, reply=""):
        self._respond = respond
        self._reply = reply

    @property
    def should_respond(self):
        return self._respond

    @property
    def reply(self):
        return self._reply

    @classmethod
    def respond_with(cls, msg: str):
        return cls(respond=True, reply=msg)

    @classmethod
    def ignore(cls):
        return cls()


def respond_to_chat(msg: ChatMessage) -> ChatDecision:
    '''
    The brains of the operation. Given the message from the chatroom, decide if we should response and what to respond
    with
    :param msg:
    :return:
    '''

    if random.random() > .5:
        return ChatDecision.respond_with(msg.author + ", you know what, mmwt")
    else:
        return ChatDecision.ignore()
