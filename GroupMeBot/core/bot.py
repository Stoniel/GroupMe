from .command import Command, command
import requests
import inspect
import importlib
import sys

GROUPME_URL = 'https://api.groupme.com/v3/bots/post'

class Bot:
    registry = {}
    extensions = {}
    cogs = {}

    def __init__(self, prefix, bot_id):
        self.prefix = prefix
        self.bot_id = bot_id

    def command(self, *args, **kwargs):
        def decorator(func):
            c = command(**kwargs)(func)
            self.add_command(c)
            return c
        return decorator

    def add_command(self, command):
        self.registry[command.name] = command
        for alias in command.aliases:
            if alias not in self.registry:
                self.registry[alias] = command

    def remove_command(self, name):
        command = self.registry.pop(name, None)

        if not command:
            return None

        if name in command.aliases:
            return command

        for alias in command.aliases:
            self.command.pop(alias, None)

        return command

    def execute(self, command, *args, **kwargs):
        c = self.registry[command]
        if c.cog:
            if not args:
                args = (c.cog,)
            else:
                args = list(args)
                args.insert(0, c.cog)

        c.execute(*args, **kwargs)

    def send_message(self, message):
        data = {
                'bot_id': self.bot_id,
                'text': message
                }
        return requests.post(GROUPME_URL, params=data)

    def load_extension(self, name):
        if name in self.extensions:
            return

        lib = importlib.import_module(name)
        if not hasattr(lib, 'setup'):
            del lib
            del sys.modules[name]
            # TODO: make custom exceptions?
            raise Exception('Extension does not have setup function')

        lib.setup(self)
        self.extensions[name] = lib

    def add_cog(self, cog):
        self.cogs[type(cog).__name__] = cog

        members = inspect.getmembers(cog)
        for name, member in members:
            if isinstance(member, Command):
                member.cog = cog
                self.add_command(member)
