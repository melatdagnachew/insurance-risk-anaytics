import pandas as pd


def missing_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Summarize missing values.
    """

    missing_count = df.isnull().sum()

    missing_percent = (
        missing_count / len(df)
    ) * 100

    summary = pd.DataFrame({
        "missing_count": missing_count,
        "missing_percent": missing_percent
    })

    return summary.sort_values(
        by="missing_percent",
        ascending=False
    )


def numerical_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Summary statistics for numerical columns.
    """

    return df.describe().T
