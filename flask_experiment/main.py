
from flask import appcontext_popped

import click
from .webapp import app


def create_app():
    return app


@click.command()
def main():
    flask_app = create_app()
    flask_app.run()
