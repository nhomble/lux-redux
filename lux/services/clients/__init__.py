import os

from lux.services.clients.groupme import GroupmeBot

GROUPME_BOT_V = "GROUPME_LUX_BOT_ID"

GROUPME_ID = os.environ.get(GROUPME_BOT_V, None)
GROUPME_BOT = GroupmeBot(GROUPME_ID)
