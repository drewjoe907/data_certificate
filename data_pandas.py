import numpy as np
import pandas as pd # primary data structure for matplotlib


df_can = pd.read_excel(
    'https://ibm.box.com/shared/static/1w190pt9zpy5bd1ptyg2aw15awomz9pu.xlsx',
    sheet_name='Canada by Citizenship',
    skiprows=range(20),
    skipfooter = 2)

df_can.head()
