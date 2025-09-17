from slack_sdk import WebClient
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv
import logging
import os
import json
import re


# Load all environment variables
load_dotenv()
socketToken = os.getenv('SOCKETTOKEN')
userToken = os.getenv('USERTOKEN')
botToken = os.getenv('BOTTOKEN')

client = WebClient(token=botToken)
