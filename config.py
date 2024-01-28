import os

API_ID = API_ID =  4942197

API_HASH = os.environ.get("API_HASH", "13248a2c551b73193969b42194023635")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6647149829:AAHWx6Wfray3vrq23VvD-0fJGKF3p0Gs6SQ")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5892781710))

LOG = -1002001856626

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5892781710").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
