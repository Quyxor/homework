from abc import ABCMeta, abstractmethod
import os
import json
import pickle


class ParamHandlerException(BaseException):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)


class ParamHandler(metaclass=ABCMeta):
    types = {}

    def __init__(self, source):
        self.source = source
        self.params = {}


    def add_param(self, key, value):
        self.params[key] = value


    def get_all_params(self):
        return self.params


    @abstractmethod
    def read(self):
        '''Чтение параметров из файла'''


    @abstractmethod
    def write(self):
        '''Запись параметров в файл'''


    @classmethod
    def add_type(cls, name, klass):
        if not name:
            raise ParamHandlerException('Type must have a name!')

        if not issubclass(klass, ParamHandler):
            raise ParamHandlerException(
                'Class "{}" is not ParamHandler!'.format(klass)
            )

        cls.types[name] = klass


    @classmethod
    def get_instance(cls, source, *args, **kwargs):
        # Шаблон "Factory method"

        _, ext = os.path.splitext(str(source).lower())
        ext = ext.lstrip('.')
        klass = cls.types.get(ext)

        if klass is None:
            raise ParamHandlerException(
                'type "{}" not found!'.format(ext)
            )

        return klass(source, *args, **kwargs)


class JsonParamHandler(ParamHandler):
    def __init__(self, source):
        super().__init__(source)


    def read(self):
        with open(self.source) as f:
            result = json.load(f)
        return result


    def write(self):
        with open(self.source, 'w') as f:
            json.dump(self.params, f, indent=4)


class PickleParamHandler(ParamHandler):
    def __init__(self, source):
        super().__init__(source)


    def read(self):
        with open(self.source, 'rb') as f:
            result = pickle.load(f)
        return result


    def write(self):
        with open(self.source, 'wb') as f:
            pickle.dump(self.params, f)


if __name__ == '__main__':
    ParamHandler.add_type("json", JsonParamHandler)
    ParamHandler.add_type("pickle", PickleParamHandler)

    pickle_config = ParamHandler.get_instance('./params.pickle')
    pickle_config.add_param('key1', 'val1')
    pickle_config.add_param('key2', 'val2')
    pickle_config.add_param('key3', 'val3')
    pickle_config.write()
    print(pickle_config.read())

    json_config = ParamHandler.get_instance('./params.json')
    json_config.add_param('key1', 'val1')
    json_config.add_param('key2', 'val2')
    json_config.add_param('key3', 'val3')
    json_config.write()
    print(json_config.read())
