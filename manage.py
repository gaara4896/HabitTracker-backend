from flask_migrate import MigrateCommand
from flask_script import Manager, Server

from app import create_app, db
#from app.apis import models

app = create_app()
app.app_context().push()
manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command("runserver", Server(host='0.0.0.0'))


@manager.command
def initdb():
    db.drop_all()
    db.create_all()


@manager.command
def list_routes():
    """List of all possible routes."""
    import urllib
    output = []
    for rule in app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        line = urllib.parse.unquote(
            "{:50s} {:20s} {}".format(rule.endpoint, methods, rule))
        output.append(line)

    for line in sorted(output):
        print(line)


@manager.command
def format():
    """Runs the yapf and isort formatters over the project."""
    isort = 'isort -rc *.py app/'
    yapf = 'yapf -r -i *.py app/'

    print('Running {}'.format(isort))
    subprocess.call(isort, shell=True)

    print('Running {}'.format(yapf))
    subprocess.call(yapf, shell=True)


if __name__ == '__main__':
    manager.run()
