
from cgitb import small
from logging import PlaceHolder
import streamlit as st
import pandas as pd
import geopandas as gpd
import numpy as np
# https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude
import geopy.distance

st.title('DSI Group Project')
st.header("Effects of Oil Refineries in Your Area")
st.subheader('Refineries in Texas')


# get our data
refineries = pd.read_csv('../datasets/refinery_coords.csv')
tract_data = gpd.read_file('../cleaned_datasets/all_data_txshp/all_data_shape.shp')
tract_data.drop(columns='geometry', inplace=True)

st.map(refineries[['latitude', 'longitude']]) # display refineries on map


# user input for their address information
user_street = st.text_input("Enter home address", placeholder='1234 Main')

if user_street != '':
    # https://stackoverflow.com/questions/25888396/how-to-get-latitude-longitude-with-python
    from geopy.geocoders import Nominatim
    geolocator = Nominatim(user_agent="my_user_agent")

    # make street info into lat/long
    loc = geolocator.geocode(user_street+',Texas,USA')

    latitude = loc.latitude
    longitude = loc.longitude
    coords = [(row['latitude'], row['longitude']) for i, row in refineries.iterrows()]

    # find distance to nearest refinery
    miles_away = min([geopy.distance.geodesic((latitude, longitude), coords[i]) for i in range(len(coords))]).miles


    # get census tract from lat/long
    from censusgeocode import CensusGeocode
    cg = CensusGeocode(vintage='Census2010_Current')
    result = cg.coordinates(x=longitude, y=latitude) #x is longitude, y is latitude

    state = result['Census Tracts'][0]['STATE']
    county = result['Census Tracts'][0]['COUNTY']
    tract = result['Census Tracts'][0]['TRACT']

    census = state+county+tract

    small_tract_data = pd.DataFrame(tract_data[tract_data['tract_num'] == int(census)][['tract_name','num_refine','total_pop','cancer_%', 'households', 'below_pove', 'hh_snap']])
    small_tract_data = small_tract_data.set_index('tract_name')
    small_tract_data.columns = ['Number of Refineries', 'Total Population', 'Percent People with Cancer', 'Number of Households', 'Households Below Poverty Line', 'Households on SNAP']

# display information

    st.subheader(f'The nearest refinery is {np.round(miles_away,2)} miles away')
    st.subheader(f'Your Census Tract Number: {census}')
    
    st.table(data=small_tract_data.transpose().style.format('{:.2f}'))

# link to tableau
link = '[Tableau](https://public.tableau.com/app/profile/vitoria.moreno.costa/viz/TexasRefineriesandCancerRisk/Dashboard2)'
st.markdown(link, unsafe_allow_html=True)

