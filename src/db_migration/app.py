from pathlib import Path

import typer
from dotenv import load_dotenv

from db_migration import fetch
from db_migration.utilities import console

cli = typer.Typer()

load_dotenv(".env")


@cli.command()
def pull(
    clean: bool = typer.Option(True, "--clean", "-c"),
    redcap_api_key: str = typer.Argument(..., envvar="REDCAP_API_KEY"),
):
    folder = Path.cwd() / "data" / "redcap"
    folder.mkdir(parents=True, exist_ok=True)
    if clean:
        console.print("Cleaning previous data...")
        for file in folder.glob("*.csv"):
            file.unlink()
        console.print("Done cleaning previous data")
    console.print("Pulling data from RedCAP...")
    fetch.download_data(api_key=redcap_api_key, folder=folder)
    console.print(f"Data is now in `{folder}`")


@cli.command()
def clean():
    pass


@cli.command()
def push():
    # push data to mongo :)
    # make sure to del first :)
    pass


@cli.command()
def greet(name: str):
    print(f"Hello {name}")
