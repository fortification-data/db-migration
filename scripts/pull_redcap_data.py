# Let's pull data from the GFDx! This can pull the most current data that the GFDx has.
# Date 8/16/2022
# requires PyCap -> 1.1.3
# Author Michelle Duong
from __future__ import annotations

from redcap import Project
from rich.progress import Progress
from rich import print
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Connecting to GFDx Redcap API
API_KEY = os.getenv("REDCAP_API_KEY", None)
if API_KEY is None:
    raise ValueError("REDCAP_API_KEY is not set")

URL = "https://redcap.emory.edu/api/"
project = Project(URL, API_KEY)

table_names = project.forms
if not table_names:
    raise ValueError("No forms found")

outdir = Path("./data/redcap", mkdir=True, parents=True)

instrument_table_names: list[str] | None = list(map(str, table_names))

with Progress(transient=True) as progress:
    task1 = progress.add_task("Downloading data...", total=len(instrument_table_names))
    for form in instrument_table_names:
        subset = project.export_records(forms=[form], format="df")
        subset.to_csv(outdir / f"{form}.csv")
        progress.advance(task1)
        progress.console.log(f"[cyan]`{form}` table downloaded")

print("[green]All data exported")
