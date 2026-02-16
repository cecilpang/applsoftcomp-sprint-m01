import marimo

__generated_with = "0.17.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import seaborn as sns
    from pathlib import Path
    return Path, mo, pd, sns


@app.cell
def _(mo):
    mo.md(r"""
    # First visualization attempt
    """)
    return


@app.cell
def _(Path, pd):
    motality_file = Path('./data/preprocessed/motality_gdp_df_20260215.csv')

    if motality_file.exists():
        print(f"The file {motality_file} exists.")
        motality_df = pd.read_csv(motality_file)
    else:
        print(f"The file {motality_file} does not exist.")

    motality_df.head(5)
    return (motality_df,)


@app.cell
def _(motality_df, sns):
    sns.scatterplot(data=motality_df, x='gdpcapita', y='motality_rate', hue='year', size='year', sizes=(10, 100))
    return


@app.cell
def _(mo):
    mo.md(r"""
    # Visualize with cleaned data
    """)
    return


@app.cell
def _(Path, motality_df, pd):
    cleaned_file = Path('./data/preprocessed/cleaned_motality_gdp_df_20260215.csv')

    if cleaned_file.exists():
        print(f"The file {cleaned_file} exists.")
        cleaned_file = pd.read_csv(cleaned_file)
    else:
        print(f"The file {cleaned_file} does not exist.")

    print(motality_df.info())
    print(cleaned_file.info())
    return (cleaned_file,)


@app.cell
def _(cleaned_file, sns):
    import matplotlib.pyplot as plt

    sns.scatterplot(data=cleaned_file, x='gdpcapita', y='motality_rate', hue='year', size='year', sizes=(10, 100))
    plt.savefig("paper/figs/scatterplot_motality_gdp.png")
    plt.show()
    return


@app.cell
def _(mo):
    mo.md(r"""
    Observations:
    1. Motality rate decreases with gdp capita increases
    2. In the old years, before 1900, mortality rates were higher and GDP was lower. Modern years, after 2000, mortality rates are lower, and GDP is higher.
    """)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
