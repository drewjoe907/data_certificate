# These Python Scripts will read some data from an xcel sheet into a panda and plotted in a number of different graphs.
# The code is organized into tasks so that it is consistent with the Coursera Lab.



# Import some useful libraries
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Get the Excel Sheet from the URL
text = pd.ExcelFile('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.xlsx')

# Declaring a useful variable
years = list(map(str, range(1980, 2014)))

# Read the excel sheet into a panda dataframe
df_can = pd.read_excel(
    text,
    sheet_name='Canada by Citizenship',
    skiprows=range(20),
    skipfooter=2)
print('Data downloaded and read into a dataframe!')

# Cleaning the data
df_can.info(verbose=False)
df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)
df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)

# Add a useful 'total' column to sum the total immigrants by country over the entire period 1980 - 2013
df_can['Total'] = df_can.sum(axis=1)

# The original index is a number range from 0-194. Setting the index to 'Country' for easy queries
df_can.set_index('Country', inplace=True)

# Switch the column names to strings (ex: 1980 -> '1980') to avoid confusion with datasets that include 1,980 entries etc.
df_can.columns = list(map(str, df_can.columns))
inplace = True # paramemter saves the changes to the original df_can dataframe

"""
    Assignment:
            Box plot -- Inter Quartile Range plotting. Create a box plot to visualize immigration from Japan to Canada
"""
df_japan = df_can.loc[['Japan'], years].transpose()
df_japan.plot(kind='box', figsize=(10, 7), color='blue', vert=False)


plt.title('Box Plot of Japanese Immigration from 1980-2013')
plt.ylabel('Number of Immigrants')
plt.show()
