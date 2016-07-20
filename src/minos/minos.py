# -*- coding: utf-8 -*-

"""minos.minos: provides entry point main()."""


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
@click.pass_context
def cli(ctx, config):
    ctx.obj = Minos(config)

@cli.command()
@click.pass_context
def config(ctx):
    click.echo(ctx.obj.config.dumps())

@cli.command()
def version():
    click.echo("Minos %s" % __version__)
    
def main():
    cli()
