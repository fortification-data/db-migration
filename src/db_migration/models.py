import enum

from pydantic import BaseModel, Field, validator


class Citation(BaseModel):
    article_author: str
    article_title: str
    article_journal: str
    article_year: int
    article_link: str
    article_citation: str
    gfdx_version: str = Field(..., alias="article_version")
    external: bool = Field(..., alias="article_external")
    internal_steward: bool = Field(..., alias="article_internal_steward")
    internal_org: bool = Field(..., alias="article_internal_org")
    has_citation: bool = Field(..., alias="article_cited")
    has_data: bool = Field(..., alias="article_data")
    revisualized: bool = Field(..., alias="article_revisualized")
    is_presentation: bool = Field(..., alias="article_presentation")
    is_report: bool = Field(..., alias="article_report")
    is_scientific: bool = Field(..., alias="article_scientific")


class FFIRegions(enum.Enum):
    Africa = 1
    Americas = 2
    Asia = 3
    Europe = 4
    India = 5
    Middle_East = 6
    Oceania = 7


class UNRegions(enum.Enum):
    Africa = 1
    Americas = 2
    Asia = 3
    Europe = 4
    Oceania = 5


class Country(BaseModel):
    name: str
    short_name: str
    redcap_country_code: int
    is_territory: bool
    ffi_region: str
    un_region: str

    @validator("ffi_region", pre=True, always=True)
    def ffi_region_validator(cls, v):
        return FFIRegions(v).name.replace("_", " ")

    @validator("un_region", pre=True, always=True)
    def un_region_validator(cls, v):
        return UNRegions(v).name.replace("_", " ")


class WBIncomeStatus(enum.Enum):
    Low = 1
    Lower_Middle = 2
    Upper_Middle = 3
    High = 4


class WBIncome(BaseModel):
    status: str
    year: int
    source: str

    @validator("status", pre=True, always=True)
    def status_validator(cls, v):
        return WBIncomeStatus(v).name.replace("_", " ")


class HealthImpact(BaseModel):
    # waiting for discussion
    pass