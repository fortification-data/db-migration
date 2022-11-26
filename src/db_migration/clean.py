import shutil
from pathlib import Path

import pandas as pd

# we can definitely make a function to filter for `arm_1` but not `all_foods_arm_1`

# we do not need to clean FF Opportunity since its all in Michelle's notebook
# we do not need to clean Summary Nutrient Intake since its useless
# we do not need to clean Nutrient Status (right now, until speaking w/ Helena) since its mostly empty
DONT_NEED_CLEANING = ["summary_nutrient_intake", "nutrition_status"]

# so we don't need to have quite as many source files as redcap
# in fact, we can check at the bottom of this script how many files we have left to clean given the above knowledge


def empty_target_dir():
    p = Path("./data/cleaned/")
    if Path("./data/cleaned/").exists():
        shutil.rmtree(p)
    Path("./data/cleaned/").mkdir(parents=True, exist_ok=True)


def clean_citations():
    target_cols = [
        "country_code",
        "article_author",
        "article_title",
        "article_journal",
        "article_year",
        "article_link",
        "article_citation",
        "article_version",
        "article_external",
        "article_internal_steward",
        "article_internal_org",
        "article_cited",
        "article_data",
        "article_revisualized",
        "article_presentation",
        "article_report",
        "article_scientific",
    ]
    pd.read_csv("./data/redcap/gfdx_citations.csv", low_memory=False).dropna()[
        target_cols
    ].to_csv("./data/cleaned/gfdx_citations.csv", index=False)


def clean_countries():
    target_cols = [
        "country_code",
        "country_name",
        "country_name_short",
        "country_territory",
        "un_region",
        "ffi_region",
    ]
    df = pd.read_csv("./data/redcap/country.csv", low_memory=False)
    df[(df["redcap_event_name"] == "all_foods_arm_1") & (df["country_code"] != 999.0)][
        target_cols
    ].to_csv("./data/cleaned/country.csv", index=False)


def clean_income_status():
    target_cols = [
        "country_code",
        "wb_income_status",
        "wb_income_status_year",
        "wb_income_status_source",
    ]
    df = pd.read_csv("./data/redcap/income_status.csv", low_memory=False)
    df[df["redcap_event_name"] == "all_foods_arm_1"][target_cols].dropna().to_csv(
        "./data/cleaned/income_status.csv", index=False
    )


def clean_population():
    target_cols = [
        "country_code",
        "population",
        "population_year",
        "population_source",
    ]
    df = pd.read_csv("./data/redcap/population.csv", low_memory=False)
    df[df["redcap_event_name"] == "all_foods_arm_1"][target_cols].dropna().to_csv(
        "./data/cleaned/population.csv", index=False
    )


def clean_urban_population():
    target_cols = [
        "country_code",
        "percent_urban",
        "percent_urban_year",
        "percent_urban_source",
    ]
    df = pd.read_csv("./data/redcap/urban_population.csv", low_memory=False)
    df[df["redcap_event_name"] == "all_foods_arm_1"][target_cols].dropna().to_csv(
        "./data/cleaned/urban_population.csv", index=False
    )


# def clean_nutrition_status():
#     # TODO: discuss with Helena and Becky
#     # for now, very simple of just making country-level
#     df = pd.read_csv("./data/redcap/nutrition_status.csv", low_memory=False)
#     df[df["redcap_event_name"] == "all_foods_arm_1"].to_csv(
#         "./data/cleaned/nutrition_status.csv", index=False
#     )


def clean_health_impact():
    df = pd.read_csv("./data/redcap/health_impact.csv", low_memory=False)
    # this can be filtered where redcap_repeat_instrument is 'health_impact'
    # and then filtered to where redcap_event_name ends with arm_1 (and NOT all_foods)
    df = df[df["redcap_repeat_instrument"] == "health_impact"].copy()
    df = df[
        (df["redcap_event_name"].str.endswith("arm_1"))
        & (df["redcap_event_name"] != "all_foods_arm_1")
    ].copy()
    df.to_csv("./data/cleaned/health_impact.csv", index=False)


def clean_foundational_documents_review():
    df = pd.read_csv(
        "./data/redcap/foundational_documents_review.csv", low_memory=False
    )
    df[
        (
            df["redcap_event_name"].str.endswith("arm_1")
            & (df["redcap_event_name"] != "all_foods_arm_1")
        )
    ].to_csv("./data/cleaned/foundational_documents_review.csv", index=False)


def clean_coverage():
    for coverage_file in Path("./data/redcap").glob("coverage_*.csv"):
        print(f"Cleaning {coverage_file.name}...")
        df = pd.read_csv(coverage_file, low_memory=False)
        df = df[
            (df["redcap_event_name"] != "all_foods_arm_1")
            & (df["redcap_event_name"].str.endswith("arm_1"))
        ].copy()
        df.to_csv(f"./data/cleaned/{coverage_file.stem}.csv", index=False)


def clean_intake():
    df = pd.read_csv("./data/redcap/intake.csv", low_memory=False)
    df = df[
        (df["redcap_event_name"] == "all_foods_arm_1")
        & (df["redcap_repeat_instrument"] == "intake")
    ].copy()
    df.to_csv("./data/cleaned/intake.csv", index=False)


def clean_availability():
    df = pd.read_csv("./data/redcap/availability.csv", low_memory=False)
    df = df[
        (
            df["redcap_event_name"].str.endswith("arm_1")
            & (df["redcap_event_name"] != "all_foods_arm_1")
        )
    ].copy()
    df.to_csv("./data/cleaned/availability.csv", index=False)


def clean_production():
    df = pd.read_csv("./data/redcap/production.csv", low_memory=False)
    df = df[
        (
            df["redcap_event_name"].str.endswith("arm_1")
            & (df["redcap_event_name"] != "all_foods_arm_1")
        )
    ].copy()
    df.to_csv("./data/cleaned/production.csv", index=False)


def clean_compliance():
    df = pd.read_csv("./data/redcap/compliance.csv", low_memory=False)
    df = df[
        (
            df["redcap_event_name"].str.endswith("arm_1")
            & (df["redcap_event_name"] != "all_foods_arm_1")
        )
    ].copy()
    df.to_csv("./data/cleaned/compliance.csv", index=False)


def clean_industrially_processed():
    df = pd.read_csv("./data/redcap/industrially_processed.csv", low_memory=False)
    df = df[
        (
            df["redcap_event_name"].str.endswith("arm_1")
            & (df["redcap_event_name"] != "all_foods_arm_1")
        )
    ].copy()
    df.to_csv("./data/cleaned/industrially_processed.csv", index=False)


def clean_legislation_status():
    df = pd.read_csv("./data/redcap/legislation_status.csv", low_memory=False)
    df = df[
        (
            df["redcap_event_name"].str.endswith("arm_1")
            & (df["redcap_event_name"] != "all_foods_arm_1")
        )
    ].copy()
    df.to_csv("./data/cleaned/legislation_status.csv", index=False)


def clean_legislation_scope():
    df = pd.read_csv("./data/redcap/legislation_scope.csv", low_memory=False)
    df = df[
        (
            df["redcap_event_name"].str.endswith("arm_1")
            & (df["redcap_event_name"] != "all_foods_arm_1")
        )
    ].copy()
    df.to_csv("./data/cleaned/legislation_scope.csv", index=False)


def clean_monitoring():
    df = pd.read_csv("./data/redcap/monitoring.csv", low_memory=False)
    df = df[
        (
            df["redcap_event_name"].str.endswith("arm_1")
            & (df["redcap_event_name"] != "all_foods_arm_1")
        )
    ].copy()
    df.to_csv("./data/cleaned/monitoring.csv", index=False)


def clean_nutrients_compounds():
    df = pd.read_csv("./data/redcap/nutrients_compounds.csv", low_memory=False)
    df = df[
        (df["redcap_repeat_instrument"] == "nutrients_compounds")
        & (
            df["redcap_event_name"].str.endswith("arm_1")
            & (df["redcap_event_name"] != "all_foods_arm_1")
        )
    ].copy()
    df.to_csv("./data/cleaned/nutrients_compounds.csv", index=False)


def clean_ff_opportunity():
    df = pd.read_csv("./data/redcap/ff_opportunity.csv", low_memory=False)
    df = df[
        (df["redcap_event_name"].str.endswith("arm_1"))
        & (df["redcap_event_name"] != "all_foods_arm_1")
    ].copy()
    df.to_csv("./data/cleaned/ff_opportunity.csv", index=False)


if __name__ == "__main__":
    print("Cleaning `clean` dir...")
    empty_target_dir()
    print("Cleaning `citations`...")
    clean_citations()
    print("Cleaning `countries`...")
    clean_countries()
    print("Cleaning `income_status`...")
    clean_income_status()
    print("Cleaning `population`...")
    clean_population()
    print("Cleaning `urban_population`...")
    clean_urban_population()
    # print("Cleaning `nutrition_status`...")
    # clean_nutrition_status()
    print("Cleaning `health_impact`...")
    clean_health_impact()
    print("Cleaning `foundational_documents_review`...")
    clean_foundational_documents_review()
    print("Cleaning `coverage`...")
    clean_coverage()
    print("Cleaning `intake`...")
    clean_intake()
    print("Cleaning `availability`...")
    clean_availability()
    print("Cleaning `production`...")
    clean_production()
    print("Cleaning `compliance`...")
    clean_compliance()
    print("Cleaning `industrially_processed`...")
    clean_industrially_processed()
    print("Cleaning `legislation_status`...")
    clean_legislation_status()
    print("Cleaning `legislation_scope`...")
    clean_legislation_scope()
    print("Cleaning `monitoring`...")
    clean_monitoring()
    print("Cleaning `nutrients_compounds`...")
    clean_nutrients_compounds()
    print("Cleaning `ff_opportunity`...")
    clean_ff_opportunity()

    source_files = len(list(Path("./data/redcap").glob("*.csv"))) - len(
        DONT_NEED_CLEANING
    )
    cleaned_files = len(list(Path("./data/cleaned").glob("*.csv")))
    print(f"Cleaned {cleaned_files} of {source_files} source files.")

    print("Done.")
