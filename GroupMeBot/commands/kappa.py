from core import command
import random

class kappa:
    def __init__(self, bot):
        self.bot = bot

    @command.command()
    def kappa(self):
        kappas = ['https://pbs.twimg.com/profile_images/1571200184/KappaHD_400x400.png',
                  'https://pbs.twimg.com/profile_images/650756757602615297/oVafDjoE.png']
        weights = [1000,1]
        kappa = random.choices(kappas,weights)
        self.bot.send_message(kappa)

def setup(bot):
    bot.add_cog(kappa(bot))
