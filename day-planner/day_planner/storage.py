import sqlite3
from .common import get_path_resourses

SQL_SELECT_ALL = '''
    SELECT
        id, number, title, description, deadline, status
    FROM
        tasks
'''

SQL_SELECT_TASK_BY_NUMBER = SQL_SELECT_ALL + ' WHERE number = ?'

SQL_SELECT_TASK_BY_TITLE = SQL_SELECT_ALL + ' WHERE title = ?'

SQL_SELECT_TASK_BY_STATUS = SQL_SELECT_ALL + ' WHERE status = ?'

SQL_INSERT_TASK = '''
    INSERT INTO tasks (number, title, deadline) VALUES (?, ?, ?)
'''

SQL_UPDATE_TASK_TITLE = '''
    UPDATE tasks SET title = ? WHERE number = ?
'''

SQL_UPDATE_TASK_DESCRIPTION = '''
    UPDATE tasks SET description = ? WHERE number = ?
'''

SQL_UPDATE_TASK_DEADLINE = '''
    UPDATE tasks SET deadline = ? WHERE number = ?
'''

SQL_UPDATE_TASK_NUMBER = '''
    UPDATE tasks SET number = ? WHERE id = ?
'''

SQL_UPDATE_TASK_STATUS = '''
    UPDATE tasks SET status = ? WHERE number = ?
'''

SQL_DELETE_TASK = '''
    DELETE FROM tasks WHERE number = ?
'''


def connect(db_name=None):
    '''Установить соединение с БД'''
    if not db_name:
        db_name = ':memory:'

    conn = sqlite3.connect(db_name)

    return conn


def initialize(conn, creation_script=None):
    '''Инициализировать структуру БД'''
    if not creation_script:
        creation_script = get_path_resourses('schema.sql')

    with conn, open(creation_script) as db_script:
        conn.executescript(db_script.read())


def add_task(conn, task_pack, domain=''):
    '''Добавить задачу в БД'''
    task = task_pack.get('task')
    deadline = task_pack.get('deadline')

    if not task:
        raise RuntimeError('Название задачи не может быть пустым.')
    if not deadline:
        raise RuntimeError('Дата окончания задачи не может быть пустой.')

    task_number = set_task_number(conn)
    cursor = conn.execute(SQL_INSERT_TASK, (task_number, task, deadline))

    return task


def get_all_tasks(conn, domain=''):
    '''Получить все добавленные задачи'''
    with conn:
        conn.row_factory = dict_factory
        cursor = conn.execute(SQL_SELECT_ALL)
        return cursor.fetchall()


def get_task_by_number(conn, task_number, domain=''):
    '''Получить задачу по номеру'''
    with conn:
        conn.row_factory = dict_factory
        cursor = conn.execute(SQL_SELECT_TASK_BY_NUMBER, (task_number,))
        return cursor.fetchall()


def delete_task_by_number(conn, task_number, domain=''):
    '''Удалить задачу'''
    if not task_number:
        raise RuntimeError('Номер задачи не может быть пустым')

    task_to_remove = get_task_by_number(conn, task_number)

    if task_to_remove:
        conn.execute(SQL_DELETE_TASK, (task_number,))
        update_task_numbers(conn)
        return task_to_remove


def set_task_number(conn, domain=''):
    '''Установить номер задачи'''
    all_tasks = get_all_tasks(conn)
    task_number = len(all_tasks)
    return task_number + 1


def update_task_numbers(conn, domain=''):
    '''Переиндексировать номера задач'''
    all_tasks = get_all_tasks(conn)

    for num, task in enumerate(all_tasks):
        conn.execute(SQL_UPDATE_TASK_NUMBER, (num + 1, task.get('id')))


def edit_task(conn, task_pack, domain=''):
    '''Изменить задачу'''
    task_number = task_pack.get('number')
    title = task_pack.get('title')
    description = task_pack.get('description')
    deadline = task_pack.get('deadline')
    status = task_pack.get('status')

    previous_task = get_task_by_number(conn, task_number)

    if not task_number:
        raise RuntimeError('Номер задачи не может быть пустым')

    if title:
        cursor = conn.execute(SQL_UPDATE_TASK_TITLE, (title, task_number))
    if description:
        conn.execute(SQL_UPDATE_TASK_DESCRIPTION, (description, task_number))
    if deadline:
        conn.execute(SQL_UPDATE_TASK_DEADLINE, (deadline, task_number))
    if status != None:
        conn.execute(SQL_UPDATE_TASK_STATUS, (status, task_number))

    changed_task = get_task_by_number(conn, task_number)

    return previous_task != changed_task


def dict_factory(cursor, row):
    '''Изменить row_factory'''
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
