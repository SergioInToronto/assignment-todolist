# TODO: actually use a database

db = {}


def list():
    return db


def save(todo_id, todo):
    db[todo_id] = todo;
    return todo

