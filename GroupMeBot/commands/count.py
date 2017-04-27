from core import command
import random

class Count:
    def __init__(self, bot):
        self.bot = bot
        self.counter = 0

    @command.command()
    def count(self):
        self.counter += 1
        self.bot.send_message(self.counter)

def setup(bot):
    bot.add_cog(Count(bot))
