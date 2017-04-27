from core import command
import random

class Tic:
    def __init__(self, bot):
        self.bot = bot
        self.array = [['_','_','_'],['_','_','_'],['_','_','_']]
        self.count = 0;

    @command.command()
    def tic(self):
        self.bot.send_message("!up,!down,!left,!right,!center,!upl,!upr,!downl,!downr")
    
    def print_array(self):
        output = '>'
        for i in self.array:
            for j in range(0, len(i)):
                output += i[j]
                if j != len(i) - 1:
                    output += '|'
            output += '\n'
        self.count+= 1
        self.bot.send_message(output)
    
    @command.command()
    def up(self):
        if self.count%2 == 0:
            self.array[0][1] = 'X'
        else:
            self.array[0][1] = 'O'
        self.print_array()
    @command.command()
    def down(self):
        if self.count % 2 == 0:
            self.array[2][1] = 'X'
        else:
            self.array[2][1] = 'O'
        self.print_array()
    @command.command()
    def left(self):
        if self.count % 2 == 0:
            self.array[1][0] = 'X'
        else:
            self.array[1][0] = 'O'
        self.print_array()
    @command.command()
    def right(self):
        if self.count % 2 == 0:
            self.array[1][2] = 'X'
        else:
            self.array[1][2] = 'O'
        self.print_array()

def setup(bot):
    bot.add_cog(Tic(bot))
