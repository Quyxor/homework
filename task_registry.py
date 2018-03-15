class Registry(object):
    __slots__ = ('__params', )

    def __init__(self):
        self.__params = {}

    def __getattribute__(self, attr):
        try:
            return super().__getattribute__(attr)
        except AttributeError:
            return self.__params.get(attr)

    def __setattr__(self, attr, value):
        try:
            return super().__setattr__(attr, value)
        except AttributeError:
            self.__params[attr] = value

    def __delattr__(self, attr):
        try:
            return super().__delattr__(attr)
        except AttributeError:
            del self.__params[attr]

    def __iter__(self):
        return iter(self.__params.items())

r = Registry()
r.kek = 123
r.check = "Hi"

for k, v in r:
   print("key: {}, value: {}".format(k, v))
