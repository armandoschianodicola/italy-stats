import pandas as pd
import geopandas as gpd

df = pd.read_csv(
    '../datasets/C_17_dataset_190_0_upFile.csv',
    delimiter=";",
    skiprows=3,
    keep_default_na=False)
print(df.head(10))
