import folium
import pandas

#Creates dataframe with csv file
df = pandas.read_csv("Volcanoes-USA.txt")
#Pandas mean function to load center of map
map = folium.Map(location=[df['LAT'].mean(),df['LON'].mean()],zoom_start=5,tiles='Mapbox bright') #list of tiles from help(folium.Map)

#if-else function to colour code volcano by elevation
def colour(elev):
    minim = int(min(df['ELEV']))
    step = int((max(df['ELEV'])- min(df['ELEV']))/3)
    if elev in range(minim,minim + step):
        col = 'green'
    elif elev in range(minim + step,minim + step*2):
        col = 'orange'
    else:
        col = 'red'
    return col

#This to toggle on-off Volcanoes
fg = folium.FeatureGroup(name ="Volcano Locations")

#for loop with df
for lat,lon,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):
    fg.add_child(folium.Marker([lat,lon],popup=name,icon=folium.Icon(color=colour(elev), icon_color = 'green'))) #check dir(folium.map.Marker) for more

#Adds the feature group
map.add_child(fg)

#using add_child function, open worldpop json file with GeoJson function
map.add_child(folium.GeoJson(data=open('worldpop.json'),
name='World Population',
style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] <= 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(folium.LayerControl())

map.save('test.html')
