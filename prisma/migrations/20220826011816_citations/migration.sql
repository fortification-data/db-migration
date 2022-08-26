-- CreateTable
CREATE TABLE "Citation" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "article_author" TEXT NOT NULL,
    "article_title" TEXT NOT NULL,
    "article_journal" TEXT NOT NULL,
    "article_year" INTEGER NOT NULL,
    "article_link" TEXT NOT NULL,
    "article_citation" TEXT NOT NULL,
    "gfdx_version" TEXT NOT NULL,
    "external" BOOLEAN NOT NULL,
    "internal_steward" BOOLEAN NOT NULL,
    "internal_org" BOOLEAN NOT NULL,
    "has_citation" BOOLEAN NOT NULL,
    "has_data" BOOLEAN NOT NULL,
    "revisualized" BOOLEAN NOT NULL,
    "is_presentation" BOOLEAN NOT NULL,
    "is_report" BOOLEAN NOT NULL,
    "is_scientific" BOOLEAN NOT NULL
);
