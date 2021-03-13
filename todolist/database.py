import json

# A full application may want db, internal logic, and views to have their own error types.
# For brevity, my db throws web-server errors directly
from werkzeug import exceptions

from todolist import database_management


database_engine = database_management.get_engine()


# Queries can be built using ORM, Table() objects, or directly as I've done below.
# I wanted to find out if writing queries myself is faster than the other 2 approaches.
# Well, it's not. It's error-prone. Using Table() objects would have been better. Lesson learned.


def list_():
    with database_engine.connect() as db_con:
        res = db_con.execute("SELECT * FROM todos")
        result = {str(x["id"]): x["contents"] for x in res}  # execute() returns lazy results. Fetch them now
    return result


def get(todo_id):
    with database_engine.connect() as db_con:
        res = db_con.execute("SELECT * FROM todos WHERE id=%s", todo_id)
    result = {str(x["id"]): x["contents"] for x in res}  # execute() returns lazy results. Fetch them now
    if not result:
        raise exceptions.NotFound(f'todo item with ID "{todo_id}" does not exist.')
    return result


def create(todo_id, todo):
    with database_engine.connect() as db_con:
        db_con.execute("INSERT INTO todos VALUES (%s, %s)", todo_id, json.dumps(todo))
    return get(todo_id)


def update(todo_id, todo):
    get(todo_id)  # throws 404 if not found
    with database_engine.connect() as db_con:
        db_con.execute("UPDATE todos SET contents=%s WHERE id=%s", json.dumps(todo), todo_id)
    return get(todo_id)


def delete(todo_id):
    with database_engine.connect() as db_con:
        db_con.execute("DELETE FROM todos WHERE id=%s", todo_id)


def delete_all_complete():
    with database_engine.connect() as db_con:
        db_con.execute("DELETE FROM todos WHERE (contents ->> 'completion')='complete'")
