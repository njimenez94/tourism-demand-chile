import pandas as pd
from data.constants import RENAME_COLS, MONTH_MAP, OUTPUT_COLS, CROSSING_NORMALIZE


def load_raw(filepath: str, sheet: str = "CONSULTA_DESAGREGADA") -> pd.DataFrame:
    """Load and rename columns from the raw SERNATUR Excel file."""
    df = pd.read_excel(filepath, sheet_name=sheet, usecols=list(RENAME_COLS.keys()))
    return df.rename(columns=RENAME_COLS)


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """Normalize text fields and build a monthly period column."""
    df = df.copy()
    for col in ("country", "region"):
        df[col] = df[col].str.strip().str.title()
    df["period"] = pd.to_datetime(
        df["year"].astype(str) + "-" + df["month"].map(MONTH_MAP).astype(str).str.zfill(2),
        format="%Y-%m",
    )
    df["crossing_detail"] = df["crossing_detail"].replace(CROSSING_NORMALIZE)
    return df.drop(columns=["year", "month"])[OUTPUT_COLS]


def process(filepath: str, save_path: str | None = None) -> pd.DataFrame:
    """Load raw SERNATUR Excel and return a cleaned, analysis-ready DataFrame."""
    df = (
        load_raw(filepath)
        .pipe(clean)
    )
    if save_path:
        df.to_parquet(save_path, index=False)
    return df
