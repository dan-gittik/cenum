import sys


class enum(object):

    default_names = None

    def __init__(self):
        super(enum, self).__init__()
        self.old = sys.gettrace()
        sys.settrace(self.tracer)

    def tracer(self, frame, event, arg):
        names = frame.f_code.co_names
        if self.default_names is None:
            self.__class__.default_names = names
        self.names = [name for name in names if name not in self.default_names]
        for name in self.names:
            frame.f_locals[name] = None
        sys.settrace(self.old)

    def __call__(self, cls):
        n = 0
        for name in self.names:
            value = getattr(cls, name)
            if isinstance(value, int):
                n = value
            setattr(cls, name, n)
            n += 1
        return cls


# Invoke enum on an empty class to capture the default attribute names.
@enum()
class _(object):
    pass
