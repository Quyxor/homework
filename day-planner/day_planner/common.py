'''
Общие методы
'''
import os.path as path
from datetime import datetime


def response_converter(response):
    '''Облагородить вид возвращаемых данных'''
    align_list = ['number', 'title', 'status']
    tmp_list = []

    for task in response:
        task['status'] = 'Открыта' if task['status'] == 0 else 'Завершена'
        tmp_list.append('\n'.join('{}:{}{}'.format(key,
                                '\t\t' if key in align_list else '\t', \
                                val) \
                                for key, val in task.items() if key != 'id'))

    return '\n\n'.join(tmp_list)


def get_path_resourses(resourse):
    return path.join(path.dirname(__file__), 'resourses', resourse)


def validate(date_text):
    try:
        datetime.strptime(date_text, '%d.%m.%Y')
        return True
    except ValueError:
        print("Некорректная дата, формат даты должен быть - DD.MM.YYYY")
        return False


def check_input(*args):
    for value in args:
        if not value:
            return False

    return True
