import marimo

__generated_with = "0.17.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    from pathlib import Path
    import pandas as pd
    return Path, mo, pd


@app.cell
def _(Path, pd):
    # load tidy files
    motality_file = Path('./data/preprocessed/child_motality_melted_20260215.csv')
    gdp_file = Path('./data/preprocessed/gdp_melted_20260215.csv')
    combined_file = Path('./data/preprocessed/motality_gdp_df_20260215.csv')
    dfs = {}

    for file_i, name_i in zip([motality_file, gdp_file, combined_file], ["motality_df", "gdp_df", "combined_df"]):
        if file_i.exists():
            print(f"The file {file_i} exists.")
            dfs[name_i] = pd.read_csv(file_i)
        else:
            print(f"The file {file_i} does not exist.")

    motality_df = dfs["motality_df"].copy()
    gdp_df = dfs["gdp_df"].copy()
    combined_df = dfs["combined_df"].copy()
    return combined_df, dfs


@app.cell
def _(dfs):
    for name, df_i in dfs.items():
        print(f"\nDataset {name}:", "-" * 50)
        print(df_i.describe())
        print('\n')
        print(df_i.info())
        print('\n')
        print(df_i.isna().sum())
    return


@app.cell
def _(mo):
    mo.md(r"""
    Observations:
    1. motality_df:
        2. 58394 observations, each row is the motality rate of a country of a year
        3. Expected Data types: "geo": str, "name": str, "year": int64, "motality_rate": float64
        4. there are null values of motality_rate, which should be excluded
    3. gdp_df:
        4. 58093 observations, each row is the gdp capita of a country of a year
        5. Note that gdp has less rows than motality. Since we will visualize mortality versus gdp, we should apply inner merge of these two datasets.
        6. Expected Data types: "geo": str, "name": str, "year": int64, "gdpcapita": float64
        7. No null values in this dataset
    8. combined_df
        9. inner merge of motality_df and gdp_df, resulting 58093 observations, each row is the motality rate, and gdp of a country of a year
        10. Expected Data types: "geo": str, "name": str, "year": int64, "motality_rate": float64, "gdpcapita": float64
        11. there are null values of motality_rate, which should be excluded
    """)
    return


@app.cell
def _(combined_df):
    # exclude nulls in combined_df
    cleaned_combined_df = combined_df.dropna()
    cleaned_combined_df.info()
    return (cleaned_combined_df,)


@app.cell
def _(cleaned_combined_df):
    # save cleaned combined data
    cleaned_combined_df.to_csv('./data/preprocessed/cleaned_motality_gdp_df_20260215.csv', index=False)
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
