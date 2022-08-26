import shutil
import pandas as pd
from pathlib import Path
from rich import print


p = Path("./data/cleaned/")
if p.exists():
    shutil.rmtree(p)

p.mkdir(exist_ok=True)

# for redcap_file in Path("./data/redcap").glob("*.csv"):
#     df = pd.read_csv(
#         redcap_file,
#         low_memory=False,
#     )
#     df.dropna(inplace=True)
#     out_path = Path("./data/cleaned") / redcap_file.name.replace(".csv", ".jsonl")
#     df.to_json(out_path, orient="records", lines=True)
#     print(f"[green]Wrote {redcap_file.name} to file.")


df = pd.read_csv(
    "./data/redcap/GFDx Citations_GlobalFortificationD_DATA_2022-08-11_1352.csv",
    low_memory=False,
)
df.dropna(inplace=True)
df.to_json("./data/cleaned/citations.jsonl", orient="records", lines=True)
print("[green]Wrote citations.jsonl to file.")
