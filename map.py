import folium


map = folium.Map(location=[38.58,-99.09],zoom_start=6, tiles="Mapbox Bright")
fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[38.18,-99.99], popup = "Hello Akki!", icon = folium.Icon(color='blue')))

map.add_child(fg)


map.save("Map1.html")
