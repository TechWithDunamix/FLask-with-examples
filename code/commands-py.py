import click
from flask.cli import with_appcontext
from models import db

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()
    click.echo('Tables created successfully!')

@click.command(name='drop_tables')
@with_appcontext
def drop_tables():
    db.drop_all()
    click.echo('Tables dropped successfully!')
