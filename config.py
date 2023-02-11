import os
from os import environ as env

class Config(object):

      BOT_TOKEN = env.get("BOT_TOKEN",'')
      API_ID = int(env.get("API_ID",'1234'))
      API_HASH = env.get("API_HASH",'')
      OWNER_ID = 5294965763

