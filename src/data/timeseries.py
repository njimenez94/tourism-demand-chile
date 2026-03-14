import pandas as pd

def build_series(
    df: pd.DataFrame,
    country: str | None = None,
    crossing_type: str | None = None,
    crossing_detail: str | None = None,
    start: str | None = None,
    end: str | None = None,
) -> pd.Series:
    """Aggregate arrivals into a monthly time series with optional filters."""
    mask = pd.Series(True, index=df.index)
    if country:
        mask &= df["country"] == country
    if crossing_type:
        mask &= df["crossing_type"] == crossing_type
    if crossing_detail:
        mask &= df["crossing_detail"] == crossing_detail
    ts = df.loc[mask].groupby("period")["arrivals"].sum().asfreq("MS").fillna(0)
    return ts.loc[start:end]