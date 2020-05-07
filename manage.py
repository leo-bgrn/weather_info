import os

from flask_script import Manager

from weather_info import create_app

env = os.getenv("FLASK_ENV") or "test"
print(f"Active environment: * {env} *")
app = create_app(env)

manager = Manager(app)
app.app_context().push()


@manager.command
def run():
    app.run()


if __name__ == "__main__":
    manager.run()
