class Command:
    def __init__(self, callback, **kwargs):

        if not callable(callback):
            raise TypeError('Callback is not callable')
        if not callback:
            raise TypeError('Callback cannot be None')

        self.callback = callback
        self.name = kwargs.get('name', callback.__name__)
        self.aliases = kwargs.get('aliases', [])
        self.description = kwargs.get('description')
        self.brief = kwargs.get('brief')
        self.help_text = kwargs.get('help_text')

    def execute(self, *args, **kwargs):
        self.callback(*args,  **kwargs)

def command(**kwargs):
    def decorator(func):
       return Command(func, **kwargs)

    return decorator
