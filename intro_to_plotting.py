# This Python Script will read some data from an xcel sheet into a panda and graph it in a number of different graphs.


# Import some useful libraries
# import piplite
# await piplite.install(['openpyxl==3.0.9'])
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# from js import fetch # Only Python with Javascript built in will run this line
import io

# Declaring a useful variables
years = list(map(str, range(1980, 2014)))

# Get the Excel Sheet from the URL
text = pd.ExcelFile('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.xlsx')

#URL = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.xlsx'
# resp = await fetch(URL)
# text = io.BytesIO((await resp.arrayBuffer()).to_py())

# Read the excel sheet into a panda
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
df_can['Total'] = df_can.sum(axis=1) # 'axis=1' for columns; 'axis=0' for rows

# The original index is a number range from 0-194. Setting the index to 'Country' for easy queries
df_can.set_index('Country', inplace=True)

# Switch the column names to strings (ex: 1980 -> '1980') to avoid confusion with datasets that include 1,980 entries etc.
df_can.columns = list(map(str, df_can.columns))


# Create a dataframe for immigration from India and China across all the years of the dataset
df_CI = df_can.loc[['India', 'China'], years]
df_CI = df_CI.transpose()
df_CI.index = df_CI.index.map(int) # let's change the index values of df_CI to type integer for plotting

df_CI.plot(kind='line')

plt.title('Immigrants from China and India')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

# plt.show()

########################### Sorting & Using & Reusing the data  ###################################################
#Step 1: Get the dataset. Recall that we created a Total column that calculates cumulative immigration by country.#
#We will sort on this column to get our top 5 countries using pandas sort_values() method.#########################

inplace = True # paramemter saves the changes to the original df_can dataframe
df_can.sort_values(by='Total', ascending=False, axis=0, inplace=True)

# get the top 5 entries
df_top5 = df_can.head(5)

# transpose the dataframe. This will be necessary when switching between graphing the columns and graphing the rows.
df_top5 = df_top5[years].transpose()



#Step 2: Plot the dataframe. To make the plot more readeable, we will change the size using the `figsize` parameter.
df_top5.index = df_top5.index.map(int) # let's change the index values of df_top5 to type integer for plotting
df_top5.plot(kind='line', figsize=(14, 8)) # pass a tuple (x, y) size



plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')


plt.show() # one of these shows function will have to be messaged out until the code is refactored into individual funcitons for each plot.

# Step 3: Sort the dataframe for an Area plot
# df_can.sort_values(['Total'], ascending = False, axis = 0, inplace = True)
