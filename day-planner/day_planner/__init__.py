from collections import OrderedDict, namedtuple
import sys

actions = OrderedDict()
action = namedtuple('Action', ['function', 'name'])


def menu_action(terminal, name):
    def decorator(function):
        actions[terminal] = action(function=function, name=name)
        return function
    return decorator


@menu_action('0', 'Вывести меню')
def show_menu():
    '''Вывести меню'''
    menu = []

    for terminal, action in actions.items():
        menu.append('{}. {}'.format(terminal, action.name))

    print('\nЕжедневник. Выберите действие:\n')
    print('\n'.join(menu))


@menu_action('1', 'Вывести список задач')
def action_show_task_list():
    '''Вывести список задач'''
    print('\nКогда-то я смогу вывести список задач')


@menu_action('2', 'Добавить задачу')
def action_add_task():
    '''Добавить задачу'''
    print('\nКогда-то я смогу добавить задачу')


@menu_action('3', 'Отредактировать задачу')
def action_edit_task():
    '''Отредактировать задачу'''
    print('\nКогда-то я смогу отредактировать задачу')


@menu_action('4', 'Завершить задачу')
def action_complete_task():
    '''Завершить задачу'''
    print('\nКогда-то я смогу завершить задачу')


@menu_action('5', 'Начать задачу сначала')
def action_restart_task():
    '''Начать задачу сначала'''
    print('\nКогда-то я смогу начать задачу сначала')


@menu_action('6', 'Выход')
def action_exit():
    '''Выход'''
    print('\nО, а это запросто, до новых встреч!')
    sys.exit(0)


def main():
    show_menu()

    while True:
        terminal = input('\nВведите число: ')
        action = actions.get(terminal)

        action.function() if action else print('\nУпс..Такой команды нет!')
