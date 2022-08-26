import pandas as pd
from pathlib import Path
from rich import print


Path("./data/cleaned/").mkdir(parents=True, exist_ok=True)

for redcap_file in Path("./data/redcap").glob("*.csv"):
    df = pd.read_csv(
        redcap_file,
        low_memory=False,
    )
    df.dropna(inplace=True)
    out_path = Path("./data/cleaned") / redcap_file.name.replace(".csv", ".jsonl")
    df.to_json(out_path, orient="records", lines=True)
    print(f"[green]Wrote {redcap_file.name} to file.")
