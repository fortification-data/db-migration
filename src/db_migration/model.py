import csv
import json
import random
from pathlib import Path
from typing import Any

import orjson
from rich import print
from rich.progress import track

# eventually use models, but for now use dict


def load_cleaned_files():
    # load all files into dict
    data = {}
    for file in Path("./data/cleaned").glob("*.jsonl"):
        with open(file, "r") as f:
            fdata = []
            for line in f:
                fdata.append(orjson.loads(line))
            data[file.stem] = fdata
    return data


def load_redcap_files() -> dict[str, Any]:
    data = {}
    for file in Path("./data/redcap").glob("*.csv"):
        print(f"Loading {file}")
        with open(file, "r") as f:
            reader = csv.DictReader(f)
            data[file.stem] = list(reader)
    return data


if __name__ == "__main__":
    # data = load_redcap_files()
    data = load_cleaned_files()
    print({k: len(v) for k, v in data.items()})
    countries = data.pop("country")
    print(len(countries))
    print(data.keys())
    # country file == base table
    unknown_tables = [
        "summary_nutrient_intake",  # this one gets DELETED COMPLETELY
    ]
    country_tables = [
        "income_status",
        # excluded because it is one variable on the country level
        # and that doesn't seem to make sense
        # "nutrition_status",
        "population",
        "urban_population",
    ]
    food_tables = [
        "availability",
        "compliance",
        "coverage_ffv",  # all coverages get combined
        "coverage_ffv_hh",  # all coverages get combined
        "coverage_ffv_hh_quant",  # all coverages get combined
        "coverage_ffv_quant",  # all coverages get combined
        "coverage_fv",  # all coverages get combined
        "coverage_ipfv",  # all coverages get combined
        "foundational_documents_review",
        "ff_opportunity",  # notebook (i.e. should be calculated)
        "health_impact",
        "industrially_processed",
        "intake",
        "legislation_scope",  # could be related to `legislation_status`?
        "legislation_status",
        "monitoring",
        # should theoretically be more nested
        # i.e. food -> nutrient -> compound
        # this is the most complicated part of our data
        "nutrients_compounds",
        "production",
    ]
    for country in track(countries):
        for c_table in country_tables:
            country[c_table] = [
                row
                for row in data[c_table]
                if row["country_code"] == country["country_code"]
            ]

        for food in ["oil", "rice", "salt", "wheat_flour", "maize_flour"]:
            country[food] = {}
            for f_table in food_tables:
                temp = [
                    row
                    for row in data[f_table]
                    if row["country_code"] == country["country_code"]
                    and row["redcap_event_name"] == f"{food}_arm_1"
                ]
                country[food][f_table] = temp
    selected = random.choice(countries)
    print(f"Selected: {selected['country_name']} w/ code: {selected['country_code']}")
    print("Sample:")
    flat_sample = {
        k: v
        for k, v in selected.items()
        if not isinstance(v, dict) and not isinstance(v, list)
    }
    print(flat_sample)

    with open("./data/countries.json", "w") as f:
        json.dump(countries, f, indent=4, sort_keys=True)

    # gfdx citations as separate collection
    with open("./data/citations.json", "w") as f:
        json.dump(data["gfdx_citations"], f, indent=4, sort_keys=True)
