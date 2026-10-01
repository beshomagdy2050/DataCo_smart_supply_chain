# DataCo Smart Supply Chain Analysis

A notebook-based analysis of delivery performance, shipping modes, regional results, profit by delivery status, and suspected-fraud orders using the DataCo Smart Supply Chain dataset.

## Project files

- `Data_Analysis_DataCo_smart_supply_chain_for_bigdata_analysis.ipynb` — analysis notebook.
- `Data_Analysis_DataCo_smart_supply_chain_for_bigdata_analysis.pbix` — Power BI report.
- `SupplyChain_Insights.xlsx` — exported analysis summaries.
- `build_database.py` — creates the SQLite database from the downloaded source CSV.
- `archive/` — source data; excluded from Git.
- `SupplyChainDB.db` — generated SQLite database; excluded from Git.

## Dataset

Download **DataCo Smart Supply Chain for Big Data Analysis** from [Kaggle](https://www.kaggle.com/datasets/shashwatwork/dataco-smart-supply-chain-for-big-data-analysis). Put `DataCoSupplyChainDataset.csv` in the project's `archive/` folder. The dataset and database are not included in this repository.

## Run the analysis

Requires Python 3.10 or newer.

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python build_database.py
jupyter lab
```

Open `Data_Analysis_DataCo_smart_supply_chain_for_bigdata_analysis.ipynb` and run all cells. The notebook reads `SupplyChainDB.db` and writes the summary workbook `SupplyChain_Insights.xlsx`.

## Tools

Python, Jupyter, pandas, NumPy, SQLite, and XlsxWriter. The Power BI report requires Microsoft Power BI Desktop.

## Notes

Run the database builder and Jupyter from the project folder. Kaggle may require an account to download the source data. Downloaded CSVs and the generated database are ignored by Git.
