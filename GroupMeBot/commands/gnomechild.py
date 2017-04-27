from core import command
import random

class GnomeChild:
    def __init__(self, bot):
        self.bot = bot

    @command.command()
    def gnomechild(self):
        gnomes = ['https://i.ytimg.com/vi/_98cfv_x8Mo/hqdefault.jpg',
                  'https://ih1.redbubble.net/image.165535751.5321/raf,750x1000,075,t,charcoal_heather.jpg',
                  'https://img.memesuper.com/cbe694aa7546edbeb8e844a9fb752b24_runescape-meme-gnome-memesuper-runescape-gnome-child-meme_1920-1080.jpeg',
                  'http://i1.kym-cdn.com/photos/images/facebook/000/813/216/e94.jpg',
                  'https://pbs.twimg.com/profile_images/614773776119648256/t-V8BO_J.png',
                  'http://i3.kym-cdn.com/photos/images/original/000/813/217/c1b.gif',
                  'https://secure.static.tumblr.com/018fefebc582dcee0f20475eea762587/z2khq8w/PMjnamruu/tumblr_static_tumblr_static_d4tsu6zs7agokwko480cwcc8c_640.png']
        gnome = random.choice(gnomes)
        self.bot.send_message(gnome)

def setup(bot):
    bot.add_cog(GnomeChild(bot))
