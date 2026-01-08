import logging
import pandas as pd
from zenml import step

class IngestData:
    """
    Ingesting the data from the data_path.
    """
    def __init__(self, data_path: str):
        """
        Args:
            data_path: Path to the data file.
        """
        self.data_path = data_path
    
    def get_data(self):
        """
        Returns:
            pd.DataFrame: Ingested data.
        """
        logging.info(f"Ingesting data from {self.data_path}")
        return pd.read_csv(self.data_path)

@step
def ingest_data(data_path: str) -> pd.DataFrame:
    """
    Ingesting the data from the data_path.

    Args:
        data_path: Path to the data file.

    Returns:
        pd.DataFrame: Ingested data.
    """
    try:
        data = IngestData(data_path=data_path)
        return data.get_data()
    except Exception as e:
        logging.error(f"Error ingesting data: {e}")
        raise e
