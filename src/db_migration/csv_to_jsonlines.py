import csv
from pathlib import Path

import orjson
from rich import print
from rich.progress import track

for file in Path("./data/cleaned").glob("*.jsonl"):
    file.unlink()

for file in track(Path("./data/cleaned").glob("*.csv")):
    with open(file, "r") as infile:
        reader = csv.DictReader(infile)
        with open(Path("./data/cleaned") / f"{file.stem}.jsonl", "w") as outfile:
            for row in reader:
                outfile.write(orjson.dumps(row).decode("utf-8") + "\n")
        print(f"Finished {file.stem}")
