class Registry(object):
    __slots__ = ('a', 'b', '__params', '__keys', '__i')

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
        self.__keys = tuple(self.__params.keys())
        self.__i = len(self.__keys)
        return self

    def __next__(self):
        if self.__i == 0:
            raise StopIteration

        self.__i -= 1

        key = self.__keys[self.__i]
        value = self.__params.get(key)

        return key, value

r = Registry()
r.kek = 123
r.check = "Hi"

for k, v in r:
   print("key: {}, value: {}".format(k, v))
