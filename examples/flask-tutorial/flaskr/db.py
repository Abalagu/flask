import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

# for type hint
from flask import Flask


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            # configuration key
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_db():
    db = get_db()
    # run SQL commands
    # after init-db command, db is reset to default, one has to re-register.
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


# work in command line
@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Initialized the database.')


# init app function is in db.py since it handles db init
def init_app(app: Flask):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
