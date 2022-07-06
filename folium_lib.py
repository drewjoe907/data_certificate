i"""
   Straight from the course: "Folium is Geodata Map Library in Python which makes mapping
   data to real world locations bing bang boom."
"""


# Import some useful libraries
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import folium
from folium import plugins

mpl.style.use('ggplot') # optional: for ggplot-like style

# Declaring a useful variable
years = list(map(str, range(1980, 2014)))

# Get the Excel Sheet from the URL
df_incidents = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Police_Department_Incidents_-_Previous_Year__2016_.csv')
print("It's lovely to see you again Druj...")

# get the first 100 crimes in the df_incidents dataframe
limit = 100
df_incidents = df_incidents.iloc[0:limit, :]

df_incidents.shape

# San Francisco latitude and longitude values
latitude = 37.77
longitude = -122.42

# let's start again with a clean copy of the map of San Francisco
sanfran_map = folium.Map(location = [latitude, longitude], zoom_start = 12)
print('Thinking about a trip to the bay?')

# instantiate a mark cluster object for the incidents in the dataframe
incidents = plugins.MarkerCluster().add_to(sanfran_map)

# loop through the dataframe and add each data point to the mark cluster
for lat, lng, label, in zip(df_incidents.Y, df_incidents.X, df_incidents.Category):
    folium.Marker(
        location=[lat, lng],
        icon=None,
        popup=label,
    ).add_to(incidents)


# save the cluster map of San Francisco crimes
sanfran_map.save("sanfran_map.html")
print('Crime follows tech. I must point you to a map I saw recently on a web page.')


# define a map centered around Mexcio with a low zoom level
#define Mexico's geolocation coordinates
mexico_latitude = 23.6345
mexico_longitude = -102.5528

# define the world map centered around Canada with a higher zoom level
mexico_map = folium.Map(location=[mexico_latitude, mexico_longitude], zoom_start=4)
print("You always loved Mexico?")
# save mexico map
# mexico_map.save('mexico_map.html')
