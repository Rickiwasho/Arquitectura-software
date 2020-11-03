from slack import WebClient
from atreidesbot import AtreidesBot
import os

# Create a slack client
slack_web_client = WebClient(token=os.environ.get("SLACK_TOKEN"))

# Get a new coinbot
atreides_bot = AtreidesBot("#playground")

# Get the onboarding message payload
message = atreides_bot.get_message_payload()

# Post the onboarding message in slack
slack_web_client.chat_postMessage(**message)
 