import pandas as pd

RENAME_COLS = {
    "AÑO": "year",
    "MES": "month",
    "NACION_01": "country",
    "REGION_01": "region",
    "PASO_02": "crossing_type",
    "PASO_01": "crossing_detail",
    "SumaDeTTAS": "arrivals",
}

MONTH_MAP = {
    "ene": 1, "feb": 2, "mar": 3, "abr": 4, "may": 5, "jun": 6,
    "jul": 7, "ago": 8, "sep": 9, "oct": 10, "nov": 11, "dic": 12,
}

OUTPUT_COLS = ["period", "region", "country", "crossing_type", "crossing_detail", "arrivals"]


def load_raw(filepath: str, sheet: str = "CONSULTA_DESAGREGADA") -> pd.DataFrame:
    """Load and rename columns from the raw SERNATUR Excel file.

    Parameters
    ----------
    filepath : str
        Path to the .xlsx file downloaded from SERNATUR.
    sheet : str
        Sheet name to read. Defaults to 'CONSULTA_DESAGREGADA'.

    Returns
    -------
    pd.DataFrame
        Raw data with standardized column names.
    """
    df = pd.read_excel(filepath, sheet_name=sheet, usecols=list(RENAME_COLS.keys()))
    return df.rename(columns=RENAME_COLS)


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """Normalize text fields and build a monthly period column.

    Returns
    -------
    pd.DataFrame
        Cleaned DataFrame with ``period`` as datetime and tidy column order.
    """
    df = df.copy()
    for col in ("country", "region"):
        df[col] = df[col].str.strip().str.title()

    df["period"] = pd.to_datetime(
        df["year"].astype(str) + "-" + df["month"].map(MONTH_MAP).astype(str).str.zfill(2),
        format="%Y-%m",
    )
    return df.drop(columns=["year", "month"])[OUTPUT_COLS]


def process(filepath: str) -> pd.DataFrame:
    """End-to-end pipeline: load → clean."""
    return clean(load_raw(filepath))


def build_series(
    df: pd.DataFrame,
    country: str,
    crossing_type: str | None = None,
    start: str | None = None,
    end: str | None = None,
) -> pd.Series:
    """Aggregate arrivals into a monthly time series for a given country.

    Parameters
    ----------
    df : pd.DataFrame
        Cleaned DataFrame from ``process()``.
    country : str
        Country name to filter (title case).
    crossing_type : str, optional
        Filter by border crossing type (e.g. 'Aéreo', 'Terrestre').
    start, end : str, optional
        Date strings to slice the series (e.g. '2015-01').

    Returns
    -------
    pd.Series
        Monthly arrivals indexed by period with freq='MS'.
    """
    mask = df["country"] == country
    if crossing_type:
        mask &= df["crossing_type"] == crossing_type

    ts = df.loc[mask].groupby("period")["arrivals"].sum().asfreq("MS").fillna(0)
    return ts.loc[start:end]