import os
'''
Здесь будут импорты нужных нам форматов файлов
'''
import json


def read_params(source):
    '''Словарь с методами чтения для различных форматов'''
    read_methods = {
                    '.txt': read,
                    '.json': load
    }

    file_format = os.path.splitext(source)[-1]
    method = read_methods.get(file_format)

    with open(source) as f:
        f.method()


def write_params(source, params):
    '''Словарь с методами записи для различных форматов'''
    wright_methods = {
                    '.txt': write,
                    '.json': dump
    }
    '''Словарь с различными форматами файлов'''
    file_formats = {
            '.txt': txt,
            '.json': json
    }

    file_extend = os.path.splitext(source)[-1]
    method = wright_methods.get(file_extend)
    file_format = file_formats.get(file_extend)

    with open(source, 'w') as f:
        file_format.method(params, f)


params = {
    'key1': 'val1',
    'key2': 'val2',
    'key3': 'val3',
}

write_params(filename, params)
read_params(filename)
