import pandas as pd
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(
    '../datasets/C_17_dataset_190_0_upFile.csv',
    delimiter=";",
    skiprows=3,
    keep_default_na=False)
np.where(df.map(lambda x: x == ''))
regions_df = gpd.read_file('../datasets/limits_IT_regions.geojson')
# df.plot.bar(x='Descrizione Regione', y='Utenti')
# regions_df.plot()
# plt.savefig('regions.png')

