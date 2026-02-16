import pandas as pd

def wide_to_long(source_path, target_path, 
                 id_vars, var_name, value_name):
    """Convert wide format to long format for raw data."""
    gdp_table = pd.read_csv(source_path)
    gdp_melted = gdp_table.melt(
        id_vars=id_vars,
        var_name=var_name,
        value_name=value_name
    )
    gdp_melted.to_csv(target_path, index=False)


if __name__ == "__main__":
    wide_to_long(
        source_path='./data/raw/gdp-data.csv',
        target_path='./data/preprocessed/gdp_tidy.csv',
        id_vars=['geo', 'name'],
        var_name='year',
        value_name='gdpcapita'
    )
    wide_to_long(
        source_path='./data/raw/child-motality.csv',
        target_path='./data/preprocessed/motality_tidy.csv',
        id_vars=['geo', 'name'],
        var_name='year',
        value_name='motality_rate'
    )