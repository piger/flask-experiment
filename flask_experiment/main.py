
from flask import appcontext_popped

import click
from .webapp import app


# fictional function that load a "static" database.
def load_db():
    db = {
        "foo": "bar",
    }
    return db

def create_app():
    app.db = load_db()
    return app

@click.command()
def main():
    flask_app = create_app()
    flask_app.run()
