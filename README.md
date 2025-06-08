# friends

check in on friends

## Setup

1. **Create and activate the virtual environment:**

   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

3. **Deactivate the environment when done:**
   ```sh
  deactivate
  ```

## Configuration

Create a `.env` file with the following variables so the scripts can send and
receive email:

```bash
GEMINI_API_KEY=your_gemini_key
GMAIL_ADDRESS=your_gmail_address
GMAIL_APP_PASSWORD=your_gmail_app_password
```

Make sure IMAP access is enabled on your Gmail account. The same credentials are
used to send the daily summary email and to check for replies.

## Adding Updates via Email

Reply to the daily "friends summary" email with one line per friend in the form
`Name: your update here`. When `reminders.py` runs, it will read any unread
replies and append those updates to `friends.yaml` under today's date.

## Running as a Daily Cron Job (Ubuntu)

If you want to automatically run `reminders.py` every morning at 8am, you can use the provided bash script to set up a cron job.

1. **Make sure your virtual environment and dependencies are set up as above.**
2. **Create the cron setup script:**

   ```sh
   ./setup_cron.sh
   ```

   This will add a cron job to run the script every day at 8am.

3. **To remove the cron job:**

   You can use the provided script:

   ```sh
   ./cancel_cron.sh
   ```

   This will remove any cron job for `reminders.py` for the current user.

## Sample Data

A sample friends YAML file is provided at `samples/sample-friends.yaml` for new users. You can use this file as a reference or starting point when creating your own `friends.yaml`.
