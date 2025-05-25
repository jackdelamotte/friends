#!/bin/bash
# Get the absolute path to this script's directory
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON="/usr/local/bin/python3"
VENV="$DIR/venv/bin/activate"
SCRIPT="$DIR/reminders.py"
LOG="$DIR/cron_reminders.log"

# Remove any existing reminders.py cron jobs for idempotency
(crontab -l 2>/dev/null | grep -v 'reminders.py'; echo "0 8 * * * source $VENV && $PYTHON $SCRIPT >> $LOG 2>&1") | crontab -

echo "Cron job set to run reminders.py every day at 8am. Output will be logged to $LOG." 
