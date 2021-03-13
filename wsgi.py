from todolist import server


application = server.build()


if __name__ == "__main__":
    application.run(debug=True)
