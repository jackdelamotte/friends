import os
import imaplib
import email
import datetime
import yaml
from load_dotenv import load_dotenv

load_dotenv()

FRIENDS_FILE = os.path.join(os.path.dirname(__file__), "friends.yaml")


def parse_updates(body: str):
    updates = {}
    for line in body.splitlines():
        line = line.strip()
        if not line or line.startswith('>') or line.lower().startswith('on ') and 'wrote:' in line:
            break
        if ':' in line:
            name, update = line.split(':', 1)
            updates[name.strip()] = update.strip()
    return updates


def update_friends_yaml(updates: dict):
    if not updates or not os.path.exists(FRIENDS_FILE):
        return
    with open(FRIENDS_FILE, "r") as f:
        friends = yaml.safe_load(f)
    today = datetime.date.today().isoformat()
    for friend in friends:
        if friend.get("name") in updates:
            if not isinstance(friend.get("personal_details"), dict):
                friend["personal_details"] = {}
            friend["personal_details"][today] = updates[friend.get("name")]
    with open(FRIENDS_FILE, "w") as f:
        yaml.safe_dump(friends, f)


def check_replies():
    imap_server = "imap.gmail.com"
    email_user = os.environ["GMAIL_ADDRESS"]
    email_pass = os.environ["GMAIL_APP_PASSWORD"]

    with imaplib.IMAP4_SSL(imap_server) as mail:
        mail.login(email_user, email_pass)
        mail.select("inbox")
        typ, data = mail.search(None, '(UNSEEN SUBJECT "Re: friends summary")')
        for num in data[0].split():
            typ, msg_data = mail.fetch(num, '(RFC822)')
            msg = email.message_from_bytes(msg_data[0][1])
            body = ""
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        charset = part.get_content_charset() or "utf-8"
                        body += part.get_payload(decode=True).decode(charset, errors='ignore')
            else:
                charset = msg.get_content_charset() or "utf-8"
                body = msg.get_payload(decode=True).decode(charset, errors='ignore')
            updates = parse_updates(body)
            update_friends_yaml(updates)
            mail.store(num, '+FLAGS', '\\Seen')
        mail.logout()


if __name__ == "__main__":
    check_replies()
