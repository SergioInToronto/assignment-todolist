# TODO: actually use a database

# import sqlalchemy
# engine = sqlalchemy.create_engine('sqlite:///:memory:', echo=True)


db = {}


# A full application may want db, internal logic, and views to have their own error types.
# For brevity, my db throws web-server-specific errors.
from werkzeug import exceptions


def list():
    return db


def get(todo_id):
    try:
        return db[todo_id]
    except KeyError:
        raise exceptions.NotFound(f'todo item with ID "{todo_id}" does not exist.')


def save(todo_id, todo):
    db[todo_id] = todo
    return todo


def delete(todo_id):
    try:
        del db[todo_id]
    except KeyError:
        raise exceptions.NotFound(f'todo item with ID "{todo_id}" does not exist.')
