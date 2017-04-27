from core import command
import requests

class Dog:

    def __init__(self, bot):
        self.bot = bot

    @command.command()
    def dog(self):
        r = requests.get('http://randomdoggiegenerator.com/randomdoggie.php')
        if r.status_code == 200:
            dog = r.json()['file']
            self.bot.send_message(cat)

def setup(bot):
    bot.add_cog(Dog(bot))
