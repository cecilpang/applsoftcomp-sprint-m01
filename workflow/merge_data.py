from pathlib import Path
import pandas as pd
import numpy as np

def dtypes(df_name) -> dict:
    datatypes = {
        "geo": str, 
        "name": str, 
        "year": np.int64, 
        "motality_rate": np.float64, 
        "gdpcapita": np.float64
    }
    if df_name == 'gdp_df':
        datatypes.pop("motality_rate")
    elif df_name == 'motality_df':
        datatypes.pop("gdpcapita")       

    return datatypes


if __name__ == "__main__":
    # load tidy files
    motality_path = Path('./data/preprocessed/motality_tidy.csv')
    gdp_path = Path('./data/preprocessed/gdp_tidy.csv')

    dfs = {}
    for path, name in zip([motality_path, gdp_path], ["motality_df", "gdp_df"]):
        if path.exists():
            print(f"The file {path} exists.")
            dfs[name] = pd.read_csv(path, dtype=dtypes(name))
        else:
            print(f"The file {path} does not exist.")

    motality_df = dfs["motality_df"].copy()
    gdp_df = dfs["gdp_df"].copy()

    # merge two tidy tables
    merged_df = motality_df.merge(gdp_df, on=['geo', 'name', 'year'], how='inner')
    merged_df = merged_df.dropna()
    merged_df.to_csv('./data/preprocessed/merged_df.csv', index=False)