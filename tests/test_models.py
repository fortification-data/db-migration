import json
from db_migration import models


def test_citation_model():
    citations: list[models.Citation] = []
    with open("./data/cleaned/citations.jsonl", "r") as f:
        for line in f:
            citations.append(models.Citation.parse_raw(line))

    assert True

    json_data = [citation.dict() for citation in citations]
    with open("./data/processed/citations.json", "w") as f:
        json.dump(json_data, f)
