# TODO: actually use a database

# import sqlalchemy
# engine = sqlalchemy.create_engine('sqlite:///:memory:', echo=True)


db = {}


def list():
    return db


def save(todo_id, todo):
    db[todo_id] = todo
    return todo
