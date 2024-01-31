# Stupid Stupid Stupid Bot
This silly lil guy literally just checks my Canvas class for a new lecture quiz and notifies a groupme chat because we are stupid and forgetful

## Usage
Set API keys CANVAS_API_URL, CANVAS_API_KEY, and BOT_ID, the first two being your school's canvas API URL and key (can be requested through canvas). The latter is a groupme developer token for a bot.
Set the COURSE variable correctly, it should match the course ID of the class you're checking for.

## How it work?
GH actions runs bot with copy of repo (On a cron job)
Bot ask canvas for assignments
Bot check if there is new assignment from canvas that is not in text file
If so, bot sends message
Bot write all assignments to text file (it was the only way I could make this work without an additional DB), noting that it has encountered a new assignment.
GH actions commits assignment file to github

## Why?
Infrequent lecture quizzes posted at weird times with little to no notififcation.
