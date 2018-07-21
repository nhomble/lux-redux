import os

from lux.services.clients.groupme import GroupmeBot

GROUPME_BOT_V = "GROUPME_LUX_BOT_ID"
GROUPME_BOT_NAME_V = "GROUPME_LUX_BOT_NAME"

GROUPME_ID = os.environ.get(GROUPME_BOT_V, None)
GROUPME_BOT_NAME = os.environ.get(GROUPME_BOT_NAME_V, None)

if GROUPME_BOT_NAME is None:
    raise RuntimeError("Must define a name")

GROUPME_BOT = GroupmeBot(GROUPME_ID, GROUPME_BOT_NAME)
