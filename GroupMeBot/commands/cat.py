from core import command
import requests


class Cat:

    def __init__(self, bot):
        self.bot = bot

    @command.command()
    def cat(self):
        r = requests.get('http://random.cat/meow')
        if r.status_code == 200:
            cat = r.json()['file']
            self.bot.send_message(cat)

def setup(bot):
    bot.add_cog(Cat(bot))
