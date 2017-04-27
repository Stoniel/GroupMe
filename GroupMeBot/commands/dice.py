from core import command
import random

class Dice:

    def __init__(self, bot):
        self.bot = bot

    @command.command(aliases=['dice'])
    def roll(self, max=6):
        max = int(max)
        self.bot.send_message(
                'You rolled {} (1,{}).'.format(
                    random.randint(1,max),
                    max)
                )

def setup(bot):
    bot.add_cog(Dice(bot))
