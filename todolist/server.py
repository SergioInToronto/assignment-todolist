import uuid

import flask

from todolist import database, view_decorators


def build():
    app = flask.Flask(__name__, static_folder="../static", static_url_path="/")
    app.add_url_rule("/", view_func=lambda: flask.redirect("/index.html", code=301))
    app.add_url_rule("/api/todos", view_func=list_todos, methods=["GET"])
    app.add_url_rule("/api/todos", view_func=create_todo, methods=["POST"])
    app.add_url_rule("/api/todos/<todo_id>", view_func=update_todo, methods=["PUT"])
    return app


def list_todos():
    return database.list()


@view_decorators.check_schema("todo_create_or_update")
def create_todo():
    todo_id = str(uuid.uuid4())
    response = database.save(todo_id, flask.request.get_json())
    return (response, 201)


@view_decorators.check_schema("todo_create_or_update")
def update_todo(todo_id):
    response = database.save(todo_id, flask.request.get_json())
    return (response, 201)
