import marimo

__generated_with = "0.17.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    return mo, pd


@app.cell
def _(mo):
    mo.md(r"""
    # Explore, Transform messy to tidy data
    """)
    return


@app.cell
def _(pd):
    # Load and tidy
    child_motality_table = pd.read_csv('./data/raw/child-motality.csv')
    child_motality_table.head(5)
    return (child_motality_table,)


@app.cell
def _(child_motality_table):
    motality_years_cols = child_motality_table.columns[2:].tolist()
    motality_years = list(map(int, motality_years_cols))
    if motality_years == list(range(1800, 2101)):
        print("child motality years range from 1800 to 2100")
    return (motality_years,)


@app.cell
def _(pd):
    gdp_table = pd.read_csv('./data/raw/gdp-data.csv')
    gdp_table.head(5)
    return (gdp_table,)


@app.cell
def _(gdp_table, motality_years):
    gdp_years_cols = gdp_table.columns[2:].tolist()
    gdp_years = list(map(int, gdp_years_cols))
    if gdp_years == motality_years:
        print("Both gdp years and child motality years range from 1800 to 2100")
    else:
        print("gdp years range different than child motality years range")
    return


@app.cell
def _(child_motality_table):
    child_motality_melted = child_motality_table.melt(
        id_vars=['geo', 'name'],
        var_name='year',
        value_name='motality_rate'
    )
    child_motality_melted.head(5)
    return (child_motality_melted,)


@app.cell
def _(gdp_table):
    gdp_melted = gdp_table.melt(
        id_vars=['geo', 'name'],
        var_name='year',
        value_name='gdpcapita'
    )
    gdp_melted.head(5)
    return (gdp_melted,)


@app.cell
def _(child_motality_melted, gdp_melted):
    # Use pd.melt(), pd.pivot_table(), or custom code
    child_motality_melted.to_csv('./data/preprocessed/child_motality_melted_20260215.csv', index=False)
    gdp_melted.to_csv('./data/preprocessed/gdp_melted_20260215.csv', index=False)
    return


@app.cell
def _(mo):
    mo.md(r"""
    # Combine two tidy tables
    """)
    return


@app.cell
def _(pd):
    from pathlib import Path

    motality_file = Path('./data/preprocessed/child_motality_melted_20260215.csv')
    gdp_file = Path('./data/preprocessed/gdp_melted_20260215.csv')
    two_dfs = {}

    for file_i, name_i in zip([motality_file, gdp_file], ["child_motality_df", "gdp_df"]):
        if file_i.exists():
            print(f"The file {file_i} exists.")
            df_i = pd.read_csv(file_i)
            two_dfs[name_i] = df_i
        else:
            print(f"The file {file_i} does not exist.")

    return (two_dfs,)


@app.cell
def _(two_dfs):
    child_motality_df = two_dfs["child_motality_df"].copy()
    gdp_df = two_dfs["gdp_df"].copy()
    return child_motality_df, gdp_df


@app.cell
def _(child_motality_df, gdp_df):
    motality_gdp_df = child_motality_df.merge(gdp_df, on=['geo', 'name', 'year'])
    motality_gdp_df
    return (motality_gdp_df,)


@app.cell
def _(motality_gdp_df):
    motality_gdp_df.to_csv('./data/preprocessed/motality_gdp_df_20260215.csv', index=False)
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
