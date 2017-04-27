# About
This is a GroupMe bot written in Python using Flask to handle
callbacks, intended to be deployed on Heroku.

## Running
You must specify the `bot_id` provided by GroupMe before running.
This can be done either by putting it in a file named `config`, or 
setting an environmental variable named `BOT_ID` to the ID.

## TODO
* Pull images from subreddits
* custom commands
* persistence on heroku's databases
* register commands with decorator
* asynchonousness
* ability to make multiple bots

