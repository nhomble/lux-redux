import requests

from lux.services import to_json


class GroupmeBot:
    URL = "https://api.groupme.com/v3/bots/post"

    def __init__(self, bot_id):
        self._bot_id = bot_id

    @property
    def bot_id(self):
        return self._bot_id

    def message(self, text, attachments=None):
        '''
        Make API request to groupme through the bot, ignore attachments for now although their API does support it
        :param text:
        :param attachments:
        :return:
        '''
        requests.post(GroupmeBot.URL, params={
            "bot_id": self.bot_id,
            "text": text
        })
