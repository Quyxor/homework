from collections import OrderedDict, namedtuple
from day_planner import storage, common
from datetime import datetime
import sys

actions = OrderedDict()
action = namedtuple('Action', ['function', 'name'])

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

    for terminal, action in actions.items():
        menu.append('{}. {}'.format(terminal, action.name))

    print('\nЕжедневник. Выберите действие:\n')
    print('\n'.join(menu))


@menu_action('1', 'Вывести список задач')
def action_show_task_list():
    '''Вывести список задач'''
    with get_connection() as conn:
        all_tasks = storage.get_all_tasks(conn)

    if all_tasks:
        print('\nСписок задач на сегодня:\n\n{}'.format(common.response_converter(all_tasks)))
    else:
        print('\nНет задач.')


@menu_action('2', 'Добавить задачу')
def action_add_task():
    '''Добавить задачу'''
    task, deadline = input('\nВведите название задачи: '), \
                     input('\nВведите дату окончания задачи: ')

    task_pack = {'task': task, 'deadline': deadline}

    with get_connection() as conn:
        added_task = storage.add_task(conn, task_pack)

    print('Ваша задача: "{}" успешно добавлена.'.format(added_task))


@menu_action('3', 'Отредактировать задачу')
def action_edit_task():
    '''Отредактировать задачу'''
    number, title, description, deadline = input('\nВведите номер задачи: '), \
                                input('\nВведите новое название задачи: '), \
                                input('\nВведите новое описание задачи: '), \
                                input('\nВведите новую дату окончания: ')
    task_pack = {'number': number,
                 'title': title,
                 'description': description,
                 'deadline': deadline
                }

    with get_connection() as conn:
        storage.edit_task(conn, task_pack)


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
    task_number = input('\nВведите номер задачи: ')
    with get_connection() as conn:
        deleted_task = storage.delete_task_by_number(conn, task_number)

    if deleted_task:
        print('\nЗадача: "{}" удалена.'.format(deleted_task))
    else:
        print('\nЗадачи под номером {} не существует.'.format(task_number))


@menu_action('7', 'Выход')
def action_exit():
    '''Выход'''
    print('\nО, а это запросто, до новых встреч!')
    sys.exit(0)


def change_status(status):
    number = input('\nВведите номер задачи: ')
    
    task_pack = {'number': number,
                 'status': status,
                }

    with get_connection() as conn:
        storage.edit_task(conn, task_pack)


def main():
    with get_connection() as conn:
        storage.initialize(conn)

    action_show_menu()

    while True:
        terminal = input('\n')
        action = actions.get(terminal)

        if action:
            action.function()
        else:
            print('\nКоманда не найдена: {}'.format(terminal))
