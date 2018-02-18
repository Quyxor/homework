from collections import OrderedDict, namedtuple
from day_planner import storage
from .common import (response_converter as resp_conv,
                    get_path_resourses as get_path,
                    validate,
                    check_input)
from datetime import datetime
from .termcolor import colored
from datetime import datetime
import sys
import os


actions = OrderedDict()
action = namedtuple('Action', ['function', 'name'])

input_task_number = lambda: input(colored('Введите номер задачи: \n', 'cyan'))
get_connection = lambda: storage.connect('tasks.sqlite3')


def menu_action(terminal, name):
    def decorator(function):
        actions[terminal] = action(function=function, name=name)
        return function
    return decorator


@menu_action('0', 'Вывести меню')
def action_show_menu():
    '''Вывести меню'''
    menu = []

    show_logo()

    for terminal, action in actions.items():
        menu.append('{}. {}'.format(terminal, action.name))

    print(colored('Ежедневник.\n\nВыберите действие:\n', 'yellow', None, ['bold']))
    print(colored('\n'.join(menu), 'green'))


@menu_action('1', 'Вывести список задач')
def action_show_task_list():
    '''Вывести список задач'''
    with get_connection() as conn:
        all_tasks = storage.get_all_tasks(conn)

    if all_tasks:
        print(colored('Список задач на сегодня:', 'yellow'))
        out_str = '\n{}\n'.format(resp_conv(all_tasks))
        print(colored(out_str, 'white'))
        print('-' * 30)
    else:
        print(colored('\nНет задач.', 'red'))


@menu_action('2', 'Добавить задачу')
def action_add_task():
    '''Добавить задачу'''
    all_input = False
    time_correct = False

    while not all_input or not time_correct:
        task, deadline = input(colored('Введите название задачи: ', 'cyan')), \
                         input(colored('\nВведите дату окончания задачи в формате DD.MM.YY: \n', 'cyan')) or datetime.now().strftime("%d.%m.%Y")

        all_input = check_input(task)
        time_correct = validate(deadline)

    task_pack = {'task': task, 'deadline': deadline}

    with get_connection() as conn:
        added_task = storage.add_task(conn, task_pack)

    print(colored('\nВаша задача: "{}" успешно добавлена.'.format(added_task), 'white'))


@menu_action('3', 'Отредактировать задачу')
def action_edit_task():
    '''Отредактировать задачу'''
    number, title, description, deadline = input_task_number(), \
    input(colored('Введите новое название задачи(не обязательно): ', 'cyan')), \
    input(colored('\nВведите новое описание задачи(не обязательно): ', 'cyan')), \
    input(colored('\nВведите новую дату окончания в формате DD.MM.YY(не обязательно): ', 'cyan'))

    task_pack = {'number': number,
                 'title': title,
                 'description': description,
                 'deadline': deadline
                }

    with get_connection() as conn:
        result = storage.edit_task(conn, task_pack)

    success_msg = colored('\nЗадача №{} успешно изменена'.format(number), 'white')
    fail_msg = colored('\nЗадача №{} не была изменена'.format(number), 'red')

    print(success_msg) if result else print(fail_msg)


@menu_action('4', 'Завершить задачу')
def action_complete_task():
    '''Завершить задачу'''
    change_status(1)


@menu_action('5', 'Начать задачу сначала')
def action_restart_task():
    '''Начать задачу сначала'''
    change_status(0)


@menu_action('6', 'Удалить задачу')
def action_delete_task():
    '''Удалить задачу'''
    task_number = input_task_number()

    with get_connection() as conn:
        deleted_task = storage.delete_task_by_number(conn, task_number)

    if deleted_task:
        print(colored('\nЗадача:\n\n{}\n\nбыла удалена.'.format(resp_conv(deleted_task)), 'white'))
    else:
        print(colored('\nЗадачи под номером {} не существует.'.format(task_number), 'red'))


@menu_action('7', 'Выход')
def action_exit():
    '''Выход'''
    print(colored('О, а это запросто, до новых встреч!', 'yellow'))
    sys.exit(0)


def change_status(status):
    '''Изменить статус задачи'''
    task_number = input_task_number()
    task_pack = {'number': task_number,
                 'status': status,
                }

    with get_connection() as conn:
        result = storage.edit_task(conn, task_pack)

    if status:
        success_msg = colored('\nЗадача №{} успешно завершена.'.format(task_number), 'white')
        fail_msg = colored('\nЗадача №{} была завершена ранее.'.format(task_number), 'red')
    else:
        success_msg = colored('\nЗадача №{} успешно переоткрыта.'.format(task_number), 'white')
        fail_msg = colored('\nЗадача №{} была переоткрыта ранее.'.format(task_number), 'red')


    print(success_msg) if result else print(fail_msg)


def show_logo():
    '''Вывести логотип программы'''
    with open(get_path('logo')) as logo:
        for line in logo:
            print(colored(line.rstrip(), 'green', None, ['bold']))


def main():
    with get_connection() as conn:
        storage.initialize(conn)

    action_show_menu()

    while True:
        terminal = input('\n')
        action = actions.get(terminal)

        if action:
            if sys.platform == 'win32':
                os.system('cls')
            else:
                os.system('clear')
                
            action.function()
        else:
            print('\nКоманда не найдена (0 - вывести меню): {}'.format(terminal))
