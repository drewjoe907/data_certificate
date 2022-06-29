# These Python Scripts will read some data from an xcel sheet into a panda and plotted in a number of different graphs.
# The code is organized into tasks so that it is consistent with the Coursera Lab.

# Import some useful libraries
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


# Declaring a useful variable
years = list(map(str, range(1980, 2014)))

# Get the Excel Sheet from the URL
text = pd.ExcelFile('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.xlsx')


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
        Create a Histogram of immigration from 195 countries in 2013. Add alpha transparency to each bar. Choose the colors. Align the bars to the ticks along the x-axis with 'xticks'
"""

count, bin_edges = np.histogram(df_can['2013']) # use numpy's histogram function to partition the spread of the data in column 2013 into 10 equal bins. Compute the number of data points that fall in each bin and then return this frequency ('count'), and the bin edges ('bin_edges')

df_can['2013'].plot(kind='hist',
                    figsize=(10, 6),
                    alpha=0.35,
                    xticks = bin_edges,
                    color=['coral', 'darkslateblue', 'mediumgreen']
                    )

plt.title('Histogram of immigration from 195 countries in 2013')
plt.ylabel('Nuber of Countries')
plt.xlabel('Number of Immigrants')
plt.show()
