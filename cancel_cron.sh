#!/bin/bash
# Remove any existing reminders.py cron jobs for the current user
(crontab -l 2>/dev/null | grep -v 'reminders.py') | crontab -
echo "Any cron job for reminders.py has been removed." 
