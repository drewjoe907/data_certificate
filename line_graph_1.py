import piplite
await piplite.install(['openpyxl==3.0.9'])
import pandas as pd
import numpy as np

from js import fetch
import io

years = list(range(1980, 2014))
URL = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.xlsx'
resp = await fetch(URL)
text = io.BytesIO((await resp.arrayBuffer()).to_py())

df_can = pd.read_excel(
    text,
    sheet_name='Canada by Citizenship',
    skiprows=range(20),
    skipfooter=2)
print('Data downloaded and read into a dataframe!')



df_can.set_index('OdName', inplace=True)

df_CI = df_can.loc[['India', 'China'], years]
df_CI
