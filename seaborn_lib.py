# Import some useful libraries
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib as mpl
import matplotlib.pyplot as plt

import seaborn as sns

print('Seaborn installed and imported!')


mpl.style.use('ggplot') # optional: for ggplot-like style

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
df_can['Total'] = df_can.sum(axis=1, numeric_only=True)

# The original index is a number range from 0-194. Setting the index to 'Country' for easy queries
df_can.set_index('Country', inplace=True)

# Switch the column names to strings (ex: 1980 -> '1980') to avoid confusion with datasets that include 1,980 entries etc.
df_can.columns = list(map(str, df_can.columns))
inplace = True # paramemter saves the changes to the original df_can dataframe

"""
    **Question**: Use seaborn to create a scatter plot with a regression line to
    visualize the total immigration from Denmark, Sweden, and Norway to Canada
    from 1980 to 2013.
"""
# let's create a new dataframe for these three countries
df_dsn = df_can.loc[['Denmark', 'Norway', 'Sweden'], years].transpose()

 # create df_total by summing across three countries for each year
df_total = pd.DataFrame(df_dsn.sum(axis=1, numeric_only=True))

# reset index in place
df_total.reset_index(inplace=True)

# rename columns
df_total.columns = ['year', 'total']

# change column year from string to int to create scatter plot
df_total['year'] = df_total['year'].astype(int)

# define figure size
plt.figure(figsize=(15, 10))

# define background style and font size
sns.set(font_scale=1.5)
sns.set_style('whitegrid')

# generate plot and add title and axes labels
ax = sns.regplot(x='year', y='total', data=df_total, color='green', marker='+', scatter_kws={'s': 200})
ax.set(xlabel='Year', ylabel='Total Immigration')
ax.set_title('Total Immigrationn from Denmark, Sweden, and Norway to Canada from 1980 - 2013')
plt.show()

"""
# we can use the sum() method to get the total population per year
df_tot = pd.DataFrame(df_can[years].sum(axis=0))

# change the years to type float (useful for regression later on)
df_tot.index = map(float, df_tot.index)

# reset the index to put in back in as a column in the df_tot dataframe
df_tot.reset_index(inplace=True)

# rename columns
df_tot.columns = ['year', 'total']

# view the final dataframe
df_tot.head()
"""


# ax = sns.regplot(x='Year', y='Total', data=df_tot)
