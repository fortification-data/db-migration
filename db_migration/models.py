from pydantic import BaseModel, Field


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
