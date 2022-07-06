"""
   Straight from the course: "A waffle chart is an interesting visualization that is normally created to display progress toward goals.
   It is commonly an effective option when you are trying to add interesting visualization features to a visual that consists mainly of
   cells, such as an Excel dashboard."
"""


# Import some useful libraries
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches # needed for waffle Charts

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
df_can['Total'] = df_can.sum(axis=1)

# The original index is a number range from 0-194. Setting the index to 'Country' for easy queries
df_can.set_index('Country', inplace=True)

# Switch the column names to strings (ex: 1980 -> '1980') to avoid confusion with datasets that include 1,980 entries etc.
df_can.columns = list(map(str, df_can.columns))
inplace = True # paramemter saves the changes to the original df_can dataframe

#  **Step 1** The first step into creating a waffle chart is determing the proportion of each category with respect to the total.

total_values = df_dsn['Total'].sum()
category_proportions = df_dsn['Total'] / total_values # compute the proportion of each category with respect to the total

#  **Step 2** The second step is defining the overall size of the waffle chart.

width = 40
height = 10
total_num_tiles = width * height

#  **Step 3** The third step is using the proportion of each category to determe it respective number of tiles

tiles_per_category = (category_proportions * total_num_tiles).round().astype(int) # compute the number of tiles for each category

#  **Step 4** The fourth step is creating a matrix that resembles the `waffle` chart and populating it.

waffle_chart = np.zeros((height, width), dtype = np.uint) # initialize the waffle chart as an empty matrix

category_index = 0
tile_index = 0 # define indices to loop through waffle chart

# populate the waffle chart
for col in range(width):
    for row in range(height):
        tile_index += 1

        # if the number of tiles populated for the current category is equal to its corresponding allocated tiles...
        if tile_index > sum(tiles_per_category[0:category_index]):
            # ...proceed to the next category
            category_index += 1

        # set the class value to an integer, which increases with class
        waffle_chart[row, col] = category_index

print ('Waffle chart populated!')

#  **Step 5** Map the waffle chart matrix into a visual & select the color scheme

fig = plt.figure() # instantiate a new figure object

# use matshow to display the waffle chart
colormap = plt.cm.coolwarm
plt.matshow(waffle_chart, cmap=colormap) # use matshow to display the waffle chart
plt.colorbar()

# **Step 6 ** Prettify the chart & add a legend.

ax = plt.gca() # get the axis

ax.set_xticks(np.arange(-.5, (width), 1), minor=True)
ax.set_yticks(np.arange(-.5, (height), 1), minor=True) # set minor ticks

ax.grid(which='minor', color='w', linestyle='-', linewidth=2) # add gridlines based on minor ticks

plt.xticks([])
plt.yticks([])

values_cumsum = np.cumsum(df_dsn['Total'])
total_values = values_cumsum[len(values_cumsum) - 1] # compute cumulative sum of individual categories to match color schemes between chart and legend

legend_handles = [] # create legend
for i, category in enumerate(df_dsn.index.values):
    label_str = category + ' (' + str(df_dsn['Total'][i]) + ')'
    color_val = colormap(float(values_cumsum[i])/total_values)
    legend_handles.append(mpatches.Patch(color=color_val, label=label_str))

plt.legend(handles=legend_handles,
           loc='lower center',
           ncol=len(df_dsn.index.values),
           bbox_to_anchor=(0., -0.2, 0.95, .1) # add legend to chart
          )
plt.show()
