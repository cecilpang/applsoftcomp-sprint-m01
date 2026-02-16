import pandas as pd
import seaborn as sns
from pathlib import Path
import matplotlib.pyplot as plt


if __name__ == "__main__":
    merged_file = Path('./data/preprocessed/merged_df.csv')
    if merged_file.exists():
        print(f"The file {merged_file} exists.")
        merged_df = pd.read_csv(merged_file)
        sns.scatterplot(data=merged_df, x='gdpcapita', y='motality_rate', hue='year', size='year', sizes=(10, 100))
        plt.savefig("./paper/figs/scatterplot_motality_gdp.png")
        plt.show()
    else:
        print(f"The file {merged_file} does not exist. Not able to create the scatter plot.")

    