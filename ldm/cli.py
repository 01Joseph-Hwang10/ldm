import os
from os import getcwd
from os.path import join
import click
from dotenv import load_dotenv
from .commands import InstallCommand
from .logger import ClickLogger


@click.group()
def cli():
    load_dotenv(dotenv_path=join(getcwd(), ".env"))


@cli.command("install")
@click.argument("dependencies", nargs=-1)
def install(dependencies: list[str]):
    debug = os.environ.get("DEBUG", None)
    logger = ClickLogger(level=1 if debug else 2)
    InstallCommand(logger=logger).run(targets=dependencies or None)
