class Event():
    def __init__(self, name):
        self.name = name
        self._listeners = []

    def emit(self, *args, **kwargs):
        for listener in self._listeners:
            listener(*args, **kwargs)

    def register(self, listener):
        if not self.is_registered(listener):
            self._listeners.append(listener)

    def deregister(self, listener):
        if self.is_registered(listener):
            self._listeners.pop(self._listeners.index(listener))

    def is_registered(self, listener):
        return listener in self._listeners

    def clear(self):
        for l in self._listeners:
            self.deregister(l)