# These Python Scripts will read some data from an xcel sheet into a panda and plotted in a number of different graphs.
# To complete your desired plot, look for the plt.show() function & uncomment it as you like. The code is organized into
# tasks so that it is consistent with the Coursera Lab.



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



#Task 1: Sort the dataframe & get save the top 5
df_can.sort_values(by='Total', ascending=False, axis=0, inplace=True)

# get the top 5 entries
df_top5 = df_can.head(5)

# transpose the dataframe. This will be necessary when switching between graphing the columns and graphing the rows.
df_top5 = df_top5[years].transpose()

df_top5.index = df_top5.index.map(int) # let's change the index values of df_top5 to type integer for plotting


# Task 2: Plot the dataframe as a linegraph.
df_top5.plot(kind='line', figsize=(14, 8)) # pass a tuple (x, y) size
plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')
# plt.show()


# Task 3: create an Area plot that tracks the immigration trends from the top 5 countries in the Dataframe

df_can.sort_values(['Total'], ascending = False, axis = 0, inplace = True)
df_top5_area = df_can.head(5)
df_top5_area = df_top5_area[years].transpose()

df_top5_area.plot(kind='area')
plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Nuber of Immigrants')
plt.xlabel('Years')
# plt.show()

# Task 4: Create a Histogram of immigration from 195 countries in 2013. Add alpha transparency to each bar. Choose the colors. Align the bars to the ticks along the x-axis with 'xticks'

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
# plt.show()

# Task 5: Creat a bar graph to track immigration from Iceland to canada from 1980-2013

df_iceland = df_can.loc['Iceland', years]
df_iceland.plot(kind='bar')

plt.title('Icelandic immigration to Canada from 1980 to 2013')
plt.ylabel('Year')
plt.xlabel('Number of Immigrants')
# plt.show()
