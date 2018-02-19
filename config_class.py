import os
'''
Здесь будут импорты нужных нам форматов файлов
'''
import json


class Configer(object):
    def __init__(self, path, params=None):
        self.path = path
        self.params = params
        '''
        Здесь появилась мысль, что можно автоматически, при инициализации
        определять формат, метод записи и метод чтения,
        аналогично функциональному методу, но мы будем иметь эти методы сразу
        self.file_format = None
        self.wright_method = None
        self.read_method = None
        '''

    def set_current_methods(self, file_format, wright_method, read_method):
        '''
        Эта функция будет рассчитывать мои переменные:
        self.file_format
        self.wright_method
        self.read_method
        По идее я бы ее еще запретил на вызов извне, чтобы не случилось чехарды
        (не реализовал еще :))
        '''
        pass


    def set_path(self, path):
        self.path = path
        '''
        Тут соответственно заново вычислять мои переменные:
        self.file_format = None
        self.wright_method = None
        self.read_method = None
        '''


    def set_params(self, params):
        self.params = params


    def get_path(self):
        return self.path


    def get_params(self):
        return self.params


    def read_file(self):
        with open(source) as f:
            self.read_method()


    def wright_file(self):
        file_format = self.file_format
        method = self.wright_method

        with open(self.path, 'w') as f:
            file_format.method(self.params, f)
