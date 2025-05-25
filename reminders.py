import json
import os
from send_email import send_email

FRIENDS_FILE = os.path.join(os.path.dirname(__file__), 'friends.json')

# Read friends.json
with open(FRIENDS_FILE, 'r') as f:
    friends = json.load(f)

# Format the details
lines = []
for friend in friends:
    details = '\n'.join(f"{k}: {v}" for k, v in friend.items())
    lines.append(details)
    lines.append("-")  # Separator

body = '\n'.join(lines)

# Send the email
send_email("friends details", body)
