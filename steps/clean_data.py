import logging
import pandas as pd
from zenml import step

@step
def clean_data(df: pd.DataFrame) -> None:
    """
    Clean the data by removing duplicates and null values.

    Args:
        df: Input DataFrame.

    Returns:
        None
    """
    pass