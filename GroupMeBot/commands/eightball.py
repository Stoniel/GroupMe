from core import command
import random

class eightball:
    def __init__(self, bot):
        self.bot = bot

    @command.command(aliases=['8ball','magicconch'])
    def eightball(self):
        ops = ['Yes',
               'No',
               'Maybe',
               'Most Likely',
               'Signs point to yes',
               'Concentrate and ask again',
               'I\'m not a learning computer',
               'Don\'t Count on it',
               'My Reply is No',
               'I\'ll make my own 8-ball! With blackjack and hookers! In fact, forget the 8-ball!',
               'Very Doubtful']
        op = random.choice(ops)
        self.bot.send_message(op)

def setup(bot):
    bot.add_cog(eightball(bot))
