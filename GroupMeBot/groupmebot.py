#!/usr/bin/env python
from core.bot import Bot
from flask import Flask, request
import os
import requests
import json

app = Flask(__name__)

bot_id = ''
try:
    bot_id = os.environ['BOT_ID']
except KeyError:
    print('no bot id')
    raise
bot = Bot('!', bot_id)

@app.route('/listener', methods=['POST'])
def listener():
    if request.method == 'POST':
        data = json.loads(request.get_data())
        text = data['text']
        if not text.startswith(bot.prefix):
            return ('', 200)

        command, *arguments = text[1:].split(' ')
        args = []
        kwargs = {}
        for arg in arguments:
            if '=' in arg:
                key,value = arg.split('=', 1)
                kwargs[key] = value
            else:
                args.append(arg)

        if command in bot.registry:
            bot.execute(command, *args, **kwargs)

        return ('', 200)

# @bot.command(name='cat', description='asdf')
# def cat():
#     r = requests.get('http://random.cat/meow')
#     if r.status_code == 200:
#         cat = r.json()['file']
#         bot.send_message(cat)

extensions = [
    'commands.cat',
    'commands.dice',
    'commands.gnomechild',
    'commands.kappa',
    'commands.eightball',
    'commands.count',
    'commands.tic'
]
for ext in extensions:
    bot.load_extension(ext)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
