import json
import os
import yaml
from send_email import send_email
from google import genai
from load_dotenv import load_dotenv
from process_replies import check_replies

load_dotenv()
check_replies()

FRIENDS_FILE = os.path.join(os.path.dirname(__file__), "friends.yaml")

# Read friends.yaml
with open(FRIENDS_FILE, "r") as f:
    friends = yaml.safe_load(f)

# Set up Gemini client
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# Summarize each friend using Gemini
summaries = []
for friend in friends:
    # Flatten personal_details dict to a string, most recent first
    details = friend.get("personal_details", {})
    if isinstance(details, dict):
        # Convert all keys to strings for sorting
        sorted_items = sorted(details.items(), key=lambda x: str(x[0]), reverse=True)
        details_str = " ".join([v for k, v in sorted_items])
    else:
        details_str = str(details)
    # Prepare a copy of friend for the prompt
    friend_for_prompt = dict(friend)
    friend_for_prompt["personal_details"] = details_str
    prompt = f"Given everything you know about this friend from the details field (most recent updates first) and our closeness (1-10), craft a message I could send them today. Please thoughtfully consider their current situation, emotional state, and any recent events—what might they need most from a friend right now? This could be encouragement, a question, an offer of help, a celebration, or simply a check-in. Avoid formulaic or repetitive responses; instead, aim for something that feels genuine, attentive, and tailored to this person. If prayer is appropriate, include it, but only if it feels natural. Keep your response to 1-2 sentences. Here is the friend's info: {json.dumps(friend_for_prompt)}"
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )
    summaries.append(response.text.strip())

body = "\n---\n".join(summaries)

# Send the email
send_email("friends summary", body)
