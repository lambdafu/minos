# -*- coding: utf-8 -*-

"""minos.minos: provides entry point main()."""


__program_name__ = "minos"
__version__ = "0.0.1"


import click
from . import Config

class Minos(object):
    def __init__(self, config=None):
        if config is None:
            # Load defaults.
            self.config = Config.fromstring("")
        else:
            with open(config) as fh:
                self.config.parse(fh)

@click.group()
@click.option("--config", envvar="MINOS_CONFIG")
@click.version_option(version=__version__, prog_name=__program_name__)
@click.pass_context
def cli(ctx, config):
    ctx.obj = Minos(config)

@cli.command(help="Print configuration.")
@click.pass_context
def config(ctx):
    click.echo(ctx.obj.config.dumps())

@cli.command(help="Start web server.")
@click.option("--host", default="127.0.0.1", help="Host to listen to.")
@click.option("--port", default=5000, help="Port to listen to.")
@click.option("--debug/--no-debug", default=False, help="Enable debug interface.")
@click.pass_context
def server(ctx, host, port, debug):
    from . server import app
    app.run(host, port, debug)

def main():
    cli()
