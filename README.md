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
