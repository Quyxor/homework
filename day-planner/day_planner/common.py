'''
Общие методы
'''
import os.path as path


def response_converter(response):
    '''Облагородить вид возвращаемых данных'''
    align_list = ['number', 'title', 'status']
    tmp_list = []

    for task in response:
        tmp_list.append('\n'.join('{}:{}{}'.format(key,
                                '\t\t' if key in align_list else '\t', \
                                val) \
                                for key, val in task.items() if key != 'id'))

    return '\n\n'.join(tmp_list)


def get_path_resourses(resourse):
    return path.join(path.dirname(__file__), 'resourses', resourse)
