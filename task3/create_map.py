"""Takes set of available markets countries names and creates map"""

import json
import folium

def create_map(market_names: set) -> None:
    """
    Creates map and fills available markets with green and unavailable with red
    Args:
        market_names (set): available countries
    """
    mapp = folium.Map(location=[45, 45],
    zoom_start=2)
    markets_availability = folium.FeatureGroup(name="Markets' availability")
    markets_availability.add_child(
        folium.GeoJson(data=open('task3/world.json', 'r', encoding='utf-8-sig').read(),
                       style_function=lambda x: {'fillColor': 'darkgreen'
                       if x['properties']['NAME'] in market_names else "darkred"}))
    markets_names = folium.FeatureGroup(name="Markets' names")
    with open('task3/world.json', 'r', encoding='utf-8-sig') as file:
        country_geo = json.loads(file.read())
        for i in country_geo['features']:
            if i['properties']['NAME'] in market_names:
                markets_names.add_child(folium.Marker(
            location=[i['properties']['LAT'],i['properties']['LON']],
            popup=i['properties']['NAME'],
            icon=folium.Icon(color="orange")))
    mapp.add_child(markets_availability)
    mapp.add_child(markets_names)
    mapp.add_child(folium.LayerControl())
    mapp.save('task3/templates/Available_markets.html')
