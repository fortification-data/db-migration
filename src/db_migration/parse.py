from pathlib import Path

import models
import orjson
import pandas as pd


def prepare_files():
    # remove all existing jsonl files in clean directory
    for file in Path("./data/cleaned").glob("*.jsonl"):
        file.unlink()
    for file in Path("../data/cleaned").glob("*.csv"):
        df: pd.DataFrame = pd.read_csv(file, low_memory=False)
        df.to_json(
            f"../data/cleaned/{file.stem}.jsonl", orient="records", lines=True
        )


# do stuff like this for each table (or use for loop to iterate over all tables)
def parse_citations():
    citations: list[models.Citation] = []
    with open("../data/cleaned/citations.jsonl", "r") as f:
        for line in f:
            citations.append(models.Citation.parse_raw(line))

    assert True

    # find better system for going from pydantic to orjson to file
    json_data = [citation.dict() for citation in citations]
    with open("../data/processed/citations.json", "w") as f:
        data = orjson.dumps(json_data)
        f.write(data.decode())



if __name__ == "__main__":
    prepare_files()

