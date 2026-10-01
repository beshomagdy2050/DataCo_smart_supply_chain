"""Build SupplyChainDB.db from the DataCo Kaggle CSV."""
from pathlib import Path
import sqlite3
import pandas as pd

ROOT = Path(__file__).resolve().parent
CSV_PATH = ROOT / "archive" / "DataCoSupplyChainDataset.csv"
DB_PATH = ROOT / "SupplyChainDB.db"

if not CSV_PATH.is_file():
    raise FileNotFoundError(
        f"Dataset not found: {CSV_PATH}\n"
        "Download DataCoSupplyChainDataset.csv from Kaggle and place it in archive/."
    )

# DataCo's file contains non-ASCII text; latin-1 safely preserves its byte values.
df = pd.read_csv(CSV_PATH, encoding="latin-1", low_memory=False)
with sqlite3.connect(DB_PATH) as connection:
    df.to_sql("SupplyChainDB", connection, if_exists="replace", index=False)

print(f"Created {DB_PATH.name} with {len(df):,} rows and {len(df.columns)} columns.")
