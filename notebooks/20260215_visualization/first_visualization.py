import marimo

__generated_with = "0.17.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import seaborn as sns
    from pathlib import Path
    return Path, pd, sns


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
    sns.scatterplot(data=motality_df[motality_df.year<=2026], x='gdpcapita', y='motality_rate', hue='year', size='year') #, sizes=(10, 100))
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
