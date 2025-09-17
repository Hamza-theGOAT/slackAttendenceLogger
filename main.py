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

# Configure Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('Attendence.log'),
        logging.StreamHandler()
    ]
)

# Load JSON Parems
with open('parem.json', 'r') as j:
    parems = json.load(j)

client = WebClient(token=botToken)
app = App(token=botToken)


@app.event("message")
def messageEvent(body, say, logger):
    print("\n" + "="*50)
    print("📩 ANY MESSAGE EVENT RECEIVED!")
    print("="*50)

    event = body.get('event', {})
    curUser = event.get('user')
    text = event.get('text', '')
    channel = event.get('channel', '')
    chnlTy = event.get('channel_type')
    subtype = event.get('subtype')
    botID = event.get('bot_id')

    if curUser in parems['attendees']:
        if 'hoorah' in text.lower():
            logging.info(f"{curUser} Marked in")
        elif 'poly' in text.lower():
            logging.info(f"{curUser} Marked out")


def main():
    print("-"*50)
    handler = SocketModeHandler(app, socketToken)
    handler.start()


if __name__ == '__main__':
    main()
