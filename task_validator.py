from abc import ABCMeta, abstractmethod
from datetime import datetime


class ValidatorException(Exception):
    '''Наследуемся для рейзов'''


class Validator(metaclass=ABCMeta):
    types = {}

    @abstractmethod
    def validate(self, value):
        ''' Возвращает булево значение'''

    @classmethod
    def add_type(cls, name, klass):
        if not name:
            raise ValidatorException('Validator must have a name!')
        elif not issubclass(klass, Validator):
            raise ValidatorException('Class "{}" is not Validator!'.format(klass))

        cls.types[name] = klass

    @classmethod
    def get_instance(cls, name):
        klass = cls.types.get(name)

        if klass is None:
            raise ValidatorException('Validator with name "{}" not found'.format(name))

        return klass()


class EMailValidator(Validator):
    def validate(self, value):
        return '@' in value


class DateTimeValidator(Validator):
    def validate(self, value):
        for key in ['%d.%m.%Y',
                    '%d.%m.%Y %H:%M',
                    '%d.%m.%Y %H:%M:%S',
                    '%Y-%m-%d',
                    '%Y-%m-%d %H:%M',
                    '%Y-%m-%d %H:%M:%S',
                    '%d/%m/%Y',
                    '%d/%m/%Y %H:%M',
                    '%d/%m/%Y %H:%M:%S'
                    ]:
            try:
                if datetime.strptime(value, key):
                    return True
            except:
                pass
        return False
