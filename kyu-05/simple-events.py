class Event:

    def __init__(self):
        self.handlers = []

    def subscribe(self, func):
        self.handlers.append(func)

    def unsubscribe(self, func):
        if func in self.handlers:
            self.handlers.remove(func)

    def emit(self, *args):
        for handler in self.handlers:
            handler(*args)
