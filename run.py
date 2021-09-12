
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from datetime import datetime #for manipulating dates and times
import datetime
import streamlit as st #to do interactive visualisation
import folium #Visualize data on map
from streamlit_folium import folium_static #link streamlit with folium
import plotly.express as px
from urllib.request import urlopen
import json
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets import make_blobs
from sklearn.neighbors import NearestNeighbors
from sklearn.cluster import DBSCAN
from geopy.distance import great_circle
import geopandas as gpd
import time
import contextily as cx

st.set_page_config(layout = "wide")

page = st.selectbox("Go To", ["Distribution of Places", "Comparison by Neighborhood", "DBSCAN"]) 
if page == "Distribution of Places":
    #Setting up the Dashboard
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
    
    st.write("If all the options are checked you can see Hotels and Tourist Attractions in this dataset distributed all over Jaipur even outside the city boundaries, therefore to maintain the validity of this analysis I reduce the data to those within the city boundaries.")
    
    #Assigning DatViz on Map
    with urlopen('https://raw.githubusercontent.com/datameet/Municipal_Spatial_Data/master/Jaipur/Jaipur_Zones.geojson') as response:
        zone_json = json.load(response)
    m = folium.Map(location=[26.922070, 75.778885], zoom_start=9,tiles='openstreetmap')
    for feature in zone_json['features']:
        feature['id'] = feature['properties']['Zone_Name']
        
    folium.GeoJson(zone_json, name="Jaipur").add_to(m)


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

    folium_static(m, width = 1450, height = 850)
    
elif page == "Comparison by Neighborhood":
    zone = pd.read_csv('zone.csv')
    geo_place = pd.read_csv ('geo_place.csv')
    geo_hotel = pd.read_csv ('geo_hotel.csv')

    #Setting up the Dashboard
    st.title('Geospatial Analysis of Tourism in Jaipur') 
    st.sidebar.subheader('Choose Comparison')

    comp_opt = ['by Review', 'by Avg. Hotel Price']
    radio_comp = st.sidebar.radio(" ",comp_opt, index = 0)


    with urlopen('https://raw.githubusercontent.com/datameet/Municipal_Spatial_Data/master/Jaipur/Jaipur_Zones.geojson') as response:
        zone_json = json.load(response)

    for feature in zone_json['features']:
        feature['id'] = feature['properties']['Zone_Name']

    if radio_comp == "by Review":
        st.write("We can assume in this case that the number of reviews is 'crowded meter' of the neighborhood, and as expected the most crowded area has the most number of the hotel, furthermore, even though tourist attractions not exactly located in the densest area it still relatively close.")
        fig = px.choropleth_mapbox(zone, color = 'NUMBER_OF_REVIEWS',
                               color_continuous_scale="OrRd",
                               geojson=zone_json,
                               locations = 'Zone_Name',
                               #mapbox_style="open-street-map",
                               zoom=10.5, center = {"lat": 26.922070, "lon": 75.778885},
                               opacity=.65,
                               labels= {'NUMBER_OF_REVIEWS': 'Number of Reviews', "Zone_Name": "Zone Name"}
                              )



    if radio_comp == "by Avg. Hotel Price":
        st.write("Be in a crowded place and in the middle of the city, doesn't make Civil Line neighborhood the most expensive area yet the most expensive neighborhood is Bagru Ansik which has an International Airport in the area. Does price have something to do with location? The Autocorrelation Spatial shows 0.09990371991295081 which means there is a slight correlation between location and the price of the hotel. ")
        fig = px.choropleth_mapbox(zone, color = 'PRICE_RUPEES',
                               color_continuous_scale="sunsetdark",
                               geojson=zone_json,
                               locations = 'Zone_Name',
                               zoom=10.5, center = {"lat": 26.922070, "lon": 75.778885},
                               opacity=.65,
                               labels= {'PRICE_RUPEES': 'Price (in Rupees)', "Zone_Name": "Zone Name"}
                              )


    fig2 = px.scatter_mapbox(geo_place, lat ='LATITUDE', lon="LONGITUDE", color_discrete_sequence = ["forestgreen"], hover_name = "POIs")
    fig3 = px.scatter_mapbox(geo_hotel, lat='Lat', lon = "Lng", hover_name = "HOTEL")


    st.sidebar.subheader('Show the distribution of:')
    hotelsct = st.sidebar.checkbox("Hotel", value = True)
    placesct = st.sidebar.checkbox("Place")

    if hotelsct:
        fig.add_trace(fig3.data[0])
    if placesct:
        fig.add_trace(fig2.data[0])

    fig.update_layout(mapbox_style='open-street-map',legend_traceorder="reversed",autosize=False, width=1450, height=850, margin=dict(l=40, r=40, b=40, t=40))

    st.plotly_chart(fig)

elif page == "DBSCAN":
    zonegpd = gpd.read_file("https://raw.githubusercontent.com/datameet/Municipal_Spatial_Data/master/Jaipur/Jaipur_Zones.geojson")
    zone = pd.read_csv('zone.csv')
    geo_place = pd.read_csv ('geo_place.csv')
    geo_hotel = pd.read_csv ('geo_hotel.csv')
    zonegpd ['city'] = 'Jaipur'
    jaipur = zonegpd[['city', 'geometry']].dissolve(by='city')
    hotel_point = geo_hotel[['Lat','Lng']].to_numpy()
    st.write("The epsilon(radius) of the DBSCAN is 1.5 Kilometer by that epsilon it can show 16 Hotel Clusters that determined by Hotel Density, The densest place is in the city center of Jaipur and the second one gathered around Jaipur International Airport")
    def get_centroid(cluster):
      """calculate the centroid of a cluster of geographic coordinate points
      Args:
        cluster coordinates, nx2 array-like (array, list of lists, etc) 
        n is the number of points(latitude, longitude)in the cluster.
      Return:
        geometry centroid of the cluster

      """
      cluster_ary = np.asarray(cluster)
      centroid = cluster_ary.mean(axis = 0)
      return centroid

    # define the number of kilometers in one radiation
    # which will be used to convert esp from km to radiation
    kms_per_rad = 6371.0088
    
    # convert eps to radians for use by haversine
    epsilon = 1.5/kms_per_rad

    # Extract intersection coordinates (latitude, longitude)
    hotels_coords = geo_hotel[['Lat', 'Lng']].values

    start_time = time.time()
    dbsc = (DBSCAN(eps=epsilon, min_samples=1, algorithm='ball_tree', metric='haversine')
            .fit(np.radians(hotels_coords)))
    hotel_cluster_labels = dbsc.labels_

    # get the number of clusters
    num_clusters = len(set(dbsc.labels_))

    # print the outcome
    message = 'Clustered {:,} points down to {:,} clusters, for {:.1f}% compression in {:,.2f} seconds'
    print(message.format(len(geo_hotel), num_clusters, 100*(1 - float(num_clusters) / len(geo_hotel)), time.time()-start_time))
    print('Silhouette coefficient: {:0.03f}'.format(metrics.silhouette_score(hotels_coords, hotel_cluster_labels)))

    # turn the clusters into a pandas series,where each element is a cluster of points
    dbsc_clusters = pd.Series([hotels_coords[hotel_cluster_labels==n] for n in range(num_clusters)])
    
    # get centroid of each cluster
    hotels_centroids = dbsc_clusters.map(get_centroid)
    # unzip the list of centroid points (lat, lon) tuples into separate lat and lon lists
    cent_lats, cent_lons = zip(*hotels_centroids)
    # from these lats/lons create a new df of one representative point for eac cluster
    centroids_pd = pd.DataFrame({'longitude':cent_lons, 'latitude':cent_lats})
    
    # Plot the faciity clusters and cluster centroid
    fig, ax = plt.subplots(figsize=[20, 12])
    hotels_scatter = ax.scatter(geo_hotel['Lng'], geo_hotel['Lat'], c=hotel_cluster_labels, cmap = cm.Dark2, edgecolor='None', alpha=0.7, s=120)
    centroid_scatter = ax.scatter(centroids_pd['longitude'], centroids_pd['latitude'], marker='x', linewidths=2, c='k', s=50)
    ax.set_title('Hotels Clusters & Hotels Centroid', fontsize = 30)
    ax.set_xlabel('Longitude', fontsize=24)
    ax.set_ylabel('Latitude', fontsize = 24)
    ax.legend([hotels_scatter, centroid_scatter], ['Hotels', 'Hotels Cluster Centroid'], loc='upper left', fontsize = 20)
    cx.add_basemap(ax, crs=jaipur.crs.to_string(), source = cx.providers.OpenStreetMap.Mapnik)
    st.pyplot(fig)
