from pathlib import Path
import sys

import pandas as pd
import polars as pl
from redcap import Project
from rich.progress import Progress

from db_migration.utilities import console


def download_data(api_key: str, folder: Path) -> None:
    # This is the part that uses PyCap to download the data
    # The package is unstable and this is an outdated version
    # because it was the only way to use the `project.forms` attribute.
    url = "https://redcap.emory.edu/api/"
    project = Project(url=url, token=api_key)
    tables = project.forms
    if tables is None:
        console.print("[red]No data found in the GFDx RedCAP project[/red]")
        console.print(
            "[red]Please check your API key or consult the database admin[/red]"
        )
        sys.exit(1)

    table_names = [str(t) for t in tables]

    with Progress(transient=True) as progress:
        task1 = progress.add_task("Downloading RedCAP data...", total=len(table_names))
        for table in table_names:
            # Here we use the defaults mostly
            # Except we specify `df` format
            df: pd.DataFrame = project.export_records(  # type: ignore (sus placement)
                forms=[table],
                format="df",
            )
            progress.console.print(f"[cyan]Downloaded {table} data[/cyan]")
            pl.from_pandas(df).write_csv(folder / f"{table}.csv")
            progress.console.print(f"[green]Saved {table} to disk[/green]")
            progress.advance(task1)

    console.print("[green]Done downloading data[/green]")
    return
