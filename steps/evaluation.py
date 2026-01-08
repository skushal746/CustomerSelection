import logging
from zenml import step
import pandas as pd

@step
def evaluate_model(df: pd.DataFrame) -> None:
    """
    Evaluate the model on the data.

    Args:
        df: Input DataFrame.

    Returns:
        None
    """
    pass