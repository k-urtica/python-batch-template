import os
from dotenv import load_dotenv

load_dotenv()

# slack
SLACK_WEBHOOK = os.environ.get("SLACK_WEBHOOK")
