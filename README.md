# Jaipur-Tourism-Geospatial-Analysis
Discovering tourism insight in Jaipur using geospatial analysis

## Data
The dataset that I used can be found in Kaggle with this [link](https://www.kaggle.com/ishikajohari/jaipur-attractions-and-hotels?select=Types.csv), the dataset is about 250 list of Jaipur Hotels with review, price and location (longitude, latitude) along with 70 Jaipur Tourist Attractions include its type, opening and closing time, location (longitude, latitude).

## Objectives
1. Discover Insights,
2. Find out density cluster of the Hotels using DBSCAN,
3. Spatial Autocorrelation Price of Hotels to find out the similarities between hotel prices and location.

## Result
* The most crowded area has the most number of the hotel, furthermore, even though tourist attractions not exactly located in the densest area it still relatively close.
* Be in a crowded place and in the middle of the city, doesn't make Civil Line neighborhood the most expensive area yet the most expensive neighborhood is Bagru Ansik which has an International Airport in the area
* The Autocorrelation Spatial shows 0.09990371991295081 which means there is a slight correlation between location and the price of the hotel.

## Dashboard App using Streamlit
You can see the result of this project [here](https://share.streamlit.io/ekassuhendar/jaipur-tourism-geospatial-analysis/main/run.py).
