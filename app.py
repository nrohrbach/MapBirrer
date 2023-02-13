import leafmap
import streamlit as st

m = leafmap.Map(center=[0, 0], zoom=2)
in_geojson = 'https://test.sharedmobility.ch/swisstopo'
m.add_geojson(in_geojson, layer_name="Cable lines")
#m


# Load a GeoJSON file
with st.echo():

    m = leafmap.Map(center=[0, 0], zoom=2)
    in_geojson = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/cable-geo.geojson'
    m.add_geojson(in_geojson, layer_name="Cable lines")
    m.to_streamlit()
