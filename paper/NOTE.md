# Relationship between child motality and GDP per capita

**Project description:** Given raw child motality and gdp data, properly re-format, clean up the dataset, then visualize the motality versus gdp. Finally draw insights from the plots.

**Source data:**
1. child-motality.csv: 
    - each row is a country's motality from year 1800 to year 2100
    - total 194 countries, 301 years 
    - there are null values of motality_rate

2. gdp-data.csv: 
    - each row is a country's gdp from year 1800 to 2100
    - total 193 countries, 301 years

**Data cleaning strategy:**
1. child_motality_melted_20260215.csv: 
    - columns of years are transformed from wide to long format, so that each row is a country's motality of a year
    - After ransform there are 58394 observations
    - Expected Data types: "geo": str, "name": str, "year": int64, "motality_rate": float64
    - To analysis the relation between motality and gdp, the null values of motality_rate are excluded

2. gdp_melted_20260215.csv: 
    - columns of years are transformed from wide to long format
    - After ransform there are 58093 observations, each row is the gdp capita of a country of a year
    - Expected Data types: "geo": str, "name": str, "year": int64, "gdpcapita": float64

3. cleaned_motality_gdp_df_20260215.csv: 
    - To analysis the relation between motality and gdp, inner merge tidy motality and gdp datasets
    - ALso exclude any null values
    - After merge and drop nulls there are 56703 data points
    - Expected Data types: "geo": str, "name": str, "year": int64, "motality_rate": float64, "gdpcapita": float64

**Visualization choices:**
Use seaborn scatterplot to plot motality versus gdp, and make "year" as hue to color years

**Key insights:**
1. There is a strong negative correlation between GDP and mortality: Motality rate decreases with gdp capita increases
2. In the old years (1800–1900), countries had low GDP levels and very high mortality rates.
3. In recent and future years, countries have low level mortality rates across countries
4. Mortality decreases steeply when GDP is at low level, indicate that small increases in GDP lead to large health improvements.
5. The curve flattens when GDP is at high level, indicates diminishing effect of GDP increasing on mortality descreasing.
