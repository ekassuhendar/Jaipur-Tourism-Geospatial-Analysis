
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from datetime import datetime #for manipulating dates and times
import datetime
import streamlit as st #to do interactive visualisation
import folium #Visualize data on map
from streamlit_folium import folium_static #link streamlit with folium

#Setting up the Dashboard
st.set_page_config(layout = "wide")
st.title('Distribution of Tourist Attractions and Hotels in Jaipur') 
st.sidebar.subheader('Choose Type(s) of Tourist Attraction')

#Assigning the Data
df_places = pd.read_csv ('Places.csv')
df_hotels = pd.read_csv ('Hotels.csv')
df_types = pd.read_csv('Types.csv')

#Replace '-' with NaN
df_places = df_places.replace('-',np.nan)
df_hotels = df_hotels.replace('-',np.nan)
df_types = df_types.replace('-',np.nan)

#Merge places dan types Data
df_merged =  pd.merge(df_places, df_types , on=["PID",'POIs'], how ='inner')

#Transform columns into datetime
df_merged['IN-TIME1'] = pd.to_datetime(df_merged['IN-TIME1'], format='%H:%M').dt.time
df_merged['OUT-TIME1'] = pd.to_datetime(df_merged['OUT-TIME1'], format='%H:%M').dt.time
df_merged['IN-TIME2'] = pd.to_datetime(df_merged['IN-TIME2'], format='%H:%M').dt.time
df_merged['OUT-TIME2'] = pd.to_datetime(df_merged['OUT-TIME2'], format='%H:%M').dt.time

#Creating checkboxes for types of tourist attraction and assigning it into variabel for if function
hiscul = st.sidebar.checkbox("History and Culture")
museum = st.sidebar.checkbox("Museum")
religious = st.sidebar.checkbox("Religious")
scenic = st.sidebar.checkbox("Scenic")
showcon = st.sidebar.checkbox("Shows and Concerts")
adventure = st.sidebar.checkbox("Adventure")
shopping = st.sidebar.checkbox("Shopping")
locex = st.sidebar.checkbox("Local Experiences")
fooddrinks = st.sidebar.checkbox("Food and Drinks")

#Assigning DatViz on Map
m = folium.Map(location=[26.922070, 75.778885], zoom_start=9,tiles='openstreetmap')

#if function for the checkboxes
if hiscul:
    for lat, lon, name, intime1, outtime1,intime2, outtime2 in zip(df_merged[df_merged['PRIORITY_1'] == 'History and Culture']['LATITUDE'], df_merged[df_merged['PRIORITY_1'] == 'History and Culture']['LONGITUDE'], df_merged[df_merged['PRIORITY_1'] == 'History and Culture']['POIs'],df_merged[df_merged['PRIORITY_1'] == 'History and Culture']['IN-TIME1'],df_merged[df_merged['PRIORITY_1'] == 'History and Culture']['OUT-TIME1'],df_merged[df_merged['PRIORITY_1'] == 'History and Culture']['IN-TIME2'],df_merged[df_merged['PRIORITY_1'] == 'History and Culture']['OUT-TIME2']):       
        folium.Marker([lat, lon],
                        popup = ('<strong>Name:</strong>: ' + str(name) + '<br>'
                                '<strong>Opening Time 1</strong>: ' + str(intime1) + '<br>'
                                '<strong>Closing Time 1</strong>: ' + str(outtime1) + '<br>'
                                '<strong>Opening Time 2</strong>: ' + str(intime2) + '<br>'
                                '<strong>Closing Time 2</strong>: ' + str(outtime2) + '<br>')).add_to(m)

if museum:
    for lat, lon, name, intime1, outtime1,intime2, outtime2 in zip(df_merged[df_merged['PRIORITY_1'] == 'Museum']['LATITUDE'], df_merged[df_merged['PRIORITY_1'] == 'Museum']['LONGITUDE'], df_merged[df_merged['PRIORITY_1'] == 'Museum']['POIs'],df_merged[df_merged['PRIORITY_1'] == 'Museum']['IN-TIME1'],df_merged[df_merged['PRIORITY_1'] == 'Museum']['OUT-TIME1'],df_merged[df_merged['PRIORITY_1'] == 'Museum']['IN-TIME2'],df_merged[df_merged['PRIORITY_1'] == 'Museum']['OUT-TIME2']):       
        folium.Marker([lat, lon],
                        popup = ('<strong>Name:</strong>: ' + str(name) + '<br>'
                                '<strong>Opening Time 1</strong>: ' + str(intime1) + '<br>'
                                '<strong>Closing Time 1</strong>: ' + str(outtime1) + '<br>'
                                '<strong>Opening Time 2</strong>: ' + str(intime2) + '<br>'
                                '<strong>Closing Time 2</strong>: ' + str(outtime2) + '<br>')).add_to(m)
        
if religious:
    for lat, lon, name, intime1, outtime1,intime2, outtime2 in zip(df_merged[df_merged['PRIORITY_1'] == 'Religious']['LATITUDE'], df_merged[df_merged['PRIORITY_1'] == 'Religious']['LONGITUDE'], df_merged[df_merged['PRIORITY_1'] == 'Religious']['POIs'],df_merged[df_merged['PRIORITY_1'] == 'Religious']['IN-TIME1'],df_merged[df_merged['PRIORITY_1'] == 'Religious']['OUT-TIME1'],df_merged[df_merged['PRIORITY_1'] == 'Religious']['IN-TIME2'],df_merged[df_merged['PRIORITY_1'] == 'Religious']['OUT-TIME2']):       
        folium.Marker([lat, lon],
                        popup = ('<strong>Name:</strong>: ' + str(name) + '<br>'
                                '<strong>Opening Time 1</strong>: ' + str(intime1) + '<br>'
                                '<strong>Closing Time 1</strong>: ' + str(outtime1) + '<br>'
                                '<strong>Opening Time 2</strong>: ' + str(intime2) + '<br>'
                                '<strong>Closing Time 2</strong>: ' + str(outtime2) + '<br>')).add_to(m)
        
if scenic:
    for lat, lon, name, intime1, outtime1,intime2, outtime2 in zip(df_merged[df_merged['PRIORITY_1'] == 'Scenic']['LATITUDE'], df_merged[df_merged['PRIORITY_1'] == 'Scenic']['LONGITUDE'], df_merged[df_merged['PRIORITY_1'] == 'Scenic']['POIs'],df_merged[df_merged['PRIORITY_1'] == 'Scenic']['IN-TIME1'],df_merged[df_merged['PRIORITY_1'] == 'Scenic']['OUT-TIME1'],df_merged[df_merged['PRIORITY_1'] == 'Scenic']['IN-TIME2'],df_merged[df_merged['PRIORITY_1'] == 'Scenic']['OUT-TIME2']):       
        folium.Marker([lat, lon],
                        popup = ('<strong>Name:</strong>: ' + str(name) + '<br>'
                                '<strong>Opening Time 1</strong>: ' + str(intime1) + '<br>'
                                '<strong>Closing Time 1</strong>: ' + str(outtime1) + '<br>'
                                '<strong>Opening Time 2</strong>: ' + str(intime2) + '<br>'
                                '<strong>Closing Time 2</strong>: ' + str(outtime2) + '<br>')).add_to(m)
        
if showcon:
    for lat, lon, name, intime1, outtime1,intime2, outtime2 in zip(df_merged[df_merged['PRIORITY_1'] == 'Shows and Concerts']['LATITUDE'], df_merged[df_merged['PRIORITY_1'] == 'Shows and Concerts']['LONGITUDE'], df_merged[df_merged['PRIORITY_1'] == 'Shows and Concerts']['POIs'],df_merged[df_merged['PRIORITY_1'] == 'Shows and Concerts']['IN-TIME1'],df_merged[df_merged['PRIORITY_1'] == 'Shows and Concerts']['OUT-TIME1'],df_merged[df_merged['PRIORITY_1'] == 'Shows and Concerts']['IN-TIME2'],df_merged[df_merged['PRIORITY_1'] == 'Shows and Concerts']['OUT-TIME2']):       
        folium.Marker([lat, lon],
                        popup = ('<strong>Name:</strong>: ' + str(name) + '<br>'
                                '<strong>Opening Time 1</strong>: ' + str(intime1) + '<br>'
                                '<strong>Closing Time 1</strong>: ' + str(outtime1) + '<br>'
                                '<strong>Opening Time 2</strong>: ' + str(intime2) + '<br>'
                                '<strong>Closing Time 2</strong>: ' + str(outtime2) + '<br>')).add_to(m)
        
if adventure:
    for lat, lon, name, intime1, outtime1,intime2, outtime2 in zip(df_merged[df_merged['PRIORITY_1'] == 'Adventure']['LATITUDE'], df_merged[df_merged['PRIORITY_1'] == 'Adventure']['LONGITUDE'], df_merged[df_merged['PRIORITY_1'] == 'Adventure']['POIs'],df_merged[df_merged['PRIORITY_1'] == 'Adventure']['IN-TIME1'],df_merged[df_merged['PRIORITY_1'] == 'Adventure']['OUT-TIME1'],df_merged[df_merged['PRIORITY_1'] == 'Adventure']['IN-TIME2'],df_merged[df_merged['PRIORITY_1'] == 'Adventure']['OUT-TIME2']):       
        folium.Marker([lat, lon],
                        popup = ('<strong>Name:</strong>: ' + str(name) + '<br>'
                                '<strong>Opening Time 1</strong>: ' + str(intime1) + '<br>'
                                '<strong>Closing Time 1</strong>: ' + str(outtime1) + '<br>'
                                '<strong>Opening Time 2</strong>: ' + str(intime2) + '<br>'
                                '<strong>Closing Time 2</strong>: ' + str(outtime2) + '<br>')).add_to(m)

if shopping:
    for lat, lon, name, intime1, outtime1,intime2, outtime2 in zip(df_merged[df_merged['PRIORITY_1'] == 'Shopping']['LATITUDE'], df_merged[df_merged['PRIORITY_1'] == 'Shopping']['LONGITUDE'], df_merged[df_merged['PRIORITY_1'] == 'Shopping']['POIs'],df_merged[df_merged['PRIORITY_1'] == 'Shopping']['IN-TIME1'],df_merged[df_merged['PRIORITY_1'] == 'Shopping']['OUT-TIME1'],df_merged[df_merged['PRIORITY_1'] == 'Shopping']['IN-TIME2'],df_merged[df_merged['PRIORITY_1'] == 'Shopping']['OUT-TIME2']):       
        folium.Marker([lat, lon],
                        popup = ('<strong>Name:</strong>: ' + str(name) + '<br>'
                                '<strong>Opening Time 1</strong>: ' + str(intime1) + '<br>'
                                '<strong>Closing Time 1</strong>: ' + str(outtime1) + '<br>'
                                '<strong>Opening Time 2</strong>: ' + str(intime2) + '<br>'
                                '<strong>Closing Time 2</strong>: ' + str(outtime2) + '<br>')).add_to(m)

if locex:
    for lat, lon, name, intime1, outtime1,intime2, outtime2 in zip(df_merged[df_merged['PRIORITY_1'] == 'Local Experiences']['LATITUDE'], df_merged[df_merged['PRIORITY_1'] == 'Local Experiences']['LONGITUDE'], df_merged[df_merged['PRIORITY_1'] == 'Local Experiences']['POIs'],df_merged[df_merged['PRIORITY_1'] == 'Local Experiences']['IN-TIME1'],df_merged[df_merged['PRIORITY_1'] == 'Local Experiences']['OUT-TIME1'],df_merged[df_merged['PRIORITY_1'] == 'Local Experiences']['IN-TIME2'],df_merged[df_merged['PRIORITY_1'] == 'Local Experiences']['OUT-TIME2']):       
        folium.Marker([lat, lon],
                        popup = ('<strong>Name:</strong>: ' + str(name) + '<br>'
                                '<strong>Opening Time 1</strong>: ' + str(intime1) + '<br>'
                                '<strong>Closing Time 1</strong>: ' + str(outtime1) + '<br>'
                                '<strong>Opening Time 2</strong>: ' + str(intime2) + '<br>'
                                '<strong>Closing Time 2</strong>: ' + str(outtime2) + '<br>')).add_to(m)
        
if fooddrinks:
    for lat, lon, name, intime1, outtime1,intime2, outtime2 in zip(df_merged[df_merged['PRIORITY_1'] == 'Food and Drinks']['LATITUDE'], df_merged[df_merged['PRIORITY_1'] == 'Food and Drinks']['LONGITUDE'], df_merged[df_merged['PRIORITY_1'] == 'Food and Drinks']['POIs'],df_merged[df_merged['PRIORITY_1'] == 'Food and Drinks']['IN-TIME1'],df_merged[df_merged['PRIORITY_1'] == 'Food and Drinks']['OUT-TIME1'],df_merged[df_merged['PRIORITY_1'] == 'Food and Drinks']['IN-TIME2'],df_merged[df_merged['PRIORITY_1'] == 'Food and Drinks']['OUT-TIME2']):       
        folium.Marker([lat, lon],
                        popup = ('<strong>Name:</strong>: ' + str(name) + '<br>'
                                '<strong>Opening Time 1</strong>: ' + str(intime1) + '<br>'
                                '<strong>Closing Time 1</strong>: ' + str(outtime1) + '<br>'
                                '<strong>Opening Time 2</strong>: ' + str(intime2) + '<br>'
                                '<strong>Closing Time 2</strong>: ' + str(outtime2) + '<br>')).add_to(m)

#Creating radio buttons
radio_options = ['Yes', 'No']
radio_hotel = st.sidebar.radio('Show Hotels?', radio_options, index = 1)

#Assign min and max PRICE RUPEES for slider of price range
min_price = min(df_hotels['PRICE_RUPEES'])
max_price = max(df_hotels['PRICE_RUPEES'])

#Categorizing popularity into 3 Categories based on its quantiles
df_hotels['Popularity'] = pd.qcut(df_hotels['NUMBER_OF_REVIEWS'][df_hotels['NUMBER_OF_REVIEWS']>0], 
                                  q=[0, .25, .75, 1], labels=['Low', 'Moderate', 'High']).astype("object")

#if function for radio buttons
if radio_hotel == 'Yes':
    #Creating slider of Price Range
    min_price_selection,max_price_selection = st.sidebar.slider('Price Range Per Night, Per Room (in Rupees)', min_value = min_price, max_value = max_price, key="2", value = [min_price,max_price])
    #Filtering data by slider
    df_hotels = df_hotels[(df_hotels['PRICE_RUPEES'] >= min_price_selection) & (df_hotels['PRICE_RUPEES'] <= max_price_selection)]
    #Creating checkboxes for Popularity
    pop_low= st.sidebar.checkbox("Low", value = True)
    pop_moderate = st.sidebar.checkbox("Moderate", value = True)
    pop_high = st.sidebar.checkbox("High", value = True)
    #if functions for checkboxes of popularity
    if pop_low:
        for hid, hotel, price, reviews, lat, long, pop in zip(df_hotels[df_hotels['Popularity'] == 'Low']['HID'], df_hotels[df_hotels['Popularity'] == 'Low']['HOTEL'], df_hotels[df_hotels['Popularity'] == 'Low']['PRICE_RUPEES'], df_hotels[df_hotels['Popularity'] == 'Low']['NUMBER_OF_REVIEWS'],df_hotels[df_hotels['Popularity'] == 'Low']['Lat'],df_hotels[df_hotels['Popularity'] == 'Low']['Lng'],df_hotels[df_hotels['Popularity'] == 'Low']['Popularity']):
            folium.Marker([lat, long],
                        popup = ('<Strong>Name:</strong> ' + str(hotel) + '<br>'
                             '<strong>Price:</strong> ' + str(price) + '<br>'
                             '<strong>Number of Reviews:</strong> ' + str(reviews) + '<br>'),
                          icon=folium.Icon(color="red",icon="hotel", prefix='fa')).add_to(m)
    if pop_moderate:
        for hid, hotel, price, reviews, lat, long, pop in zip(df_hotels[df_hotels['Popularity'] == 'Moderate']['HID'], df_hotels[df_hotels['Popularity'] == 'Moderate']['HOTEL'], df_hotels[df_hotels['Popularity'] == 'Moderate']['PRICE_RUPEES'], df_hotels[df_hotels['Popularity'] == 'Moderate']['NUMBER_OF_REVIEWS'],df_hotels[df_hotels['Popularity'] == 'Moderate']['Lat'],df_hotels[df_hotels['Popularity'] == 'Moderate']['Lng'],df_hotels[df_hotels['Popularity'] == 'Moderate']['Popularity']):
            folium.Marker([lat, long],
                        popup = ('<Strong>Name:</strong> ' + str(hotel) + '<br>'
                             '<strong>Price:</strong> ' + str(price) + '<br>'
                             '<strong>Number of Reviews:</strong> ' + str(reviews) + '<br>'),
                          icon=folium.Icon(color="red",icon="hotel", prefix='fa')).add_to(m)
    if pop_high:
        for hid, hotel, price, reviews, lat, long, pop in zip(df_hotels[df_hotels['Popularity'] == 'High']['HID'], df_hotels[df_hotels['Popularity'] == 'High']['HOTEL'], df_hotels[df_hotels['Popularity'] == 'High']['PRICE_RUPEES'], df_hotels[df_hotels['Popularity'] == 'High']['NUMBER_OF_REVIEWS'],df_hotels[df_hotels['Popularity'] == 'High']['Lat'],df_hotels[df_hotels['Popularity'] == 'High']['Lng'],df_hotels[df_hotels['Popularity'] == 'High']['Popularity']):
            folium.Marker([lat, long],
                        popup = ('<Strong>Name:</strong> ' + str(hotel) + '<br>'
                             '<strong>Price:</strong> ' + str(price) + '<br>'
                             '<strong>Number of Reviews:</strong> ' + str(reviews) + '<br>'),
                          icon=folium.Icon(color="red",icon="hotel", prefix='fa')).add_to(m)
            
folium_static(m, width = 1600, height = 950)
