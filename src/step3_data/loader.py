import pandas as pd
from step2_utils.logger import get_logger

logger=get_logger(__name__)

def load_dataset(path, max_samples=None):
    logger.info(f"Loading dataset from {path}")
    df=pd.read_csv(path)

    cols=["question1","question2"]
    if "is_duplicate" in df.columns:
        cols.append("is_duplicate")

    df=df.dropna(subset=cols)
    df=df[cols]

    if max_samples:
        df=df.sample(max_samples,random_state=42)
    logger.info(f"Loaded {len(df)} rows")

    return df