from __future__ import annotations

import csv
import os
from pathlib import Path
import sys
from typing import Any

from dotenv import load_dotenv
from redcap import Project
from rich.progress import Progress
from utilities import console


def download_data() -> None:
    load_dotenv()
    # This is the part that uses PyCap to download the data
    # The package is unstable and this is an outdated version
    # because it was the only way to use the `project.forms` attribute.
    url = "https://redcap.emory.edu/api/"
    api_key = os.environ.get("REDCAP_API_KEY")
    if api_key is None:
        console.log("[red]REDCAP_API_KEY[/red] environment variable not set.")
        sys.exit(1)
    project = Project(url=url, token=api_key)

    tables: tuple[str] | None = project.forms
    if tables is None:
        console.log("[red]No data found in the GFDx RedCAP project[/red]")
        console.log(
            "[red]Please check your API key or consult the database admin[/red]"
        )
        sys.exit(1)

    out_dir = Path("data") / "redcap"
    out_dir.mkdir(parents=True, exist_ok=True)

    with Progress(transient=True) as progress:
        task1 = progress.add_task("Downloading RedCAP data into `data/redcap` folder...", total=len(tables))
        for table in tables:
            # Here we use the defaults mostly
            # Except we specify `df` format
            data: list[dict[str, Any]] = project.export_records(forms=[table])
            if len(data) == 0:
                progress.console.log(f"[red]No data found in {table}[/red]")
                continue

            with open(out_dir / f"{table}.csv", "w") as f:
                csvwriter = csv.DictWriter(f, fieldnames=data[0].keys())
                csvwriter.writeheader()
                csvwriter.writerows(data)

            progress.console.log(f"[green]Saved `{table}` to disk[/green]")
            progress.advance(task1)

    console.log("[green]Done![/green]")


if __name__ == "__main__":
    download_data()
