import folium

# Existing pipelines map.
m = folium.Map(location=[-22.575567970590456, 133.41701195],zoom_start=4)

folium.GeoJson(data='../data/existing_gas_pipelines.geojson', name="Existing gas pipelines", style_function= lambda feature: {
        'color': 'orange'
    },tooltip=folium.GeoJsonTooltip(fields=['NAME', 'FEATURE_TYPE'])).add_to(m)

folium.GeoJson(data='../data/existing_oil_pipelines.geojson', name="Existing oil pipelines", style_function=lambda feature: {
        'color': 'red'
    }, tooltip=folium.GeoJsonTooltip(fields=['NAME', 'FEATURE_TYPE'])).add_to(m)

folium.LayerControl(collapsed=False).add_to(m)
m.save("../html/existing_pipelines.html")

# Proposed pipelines map.
m = folium.Map(location=[-22.575567970590456, 133.41701195],zoom_start=4)

folium.GeoJson(data='../data/proposed_gas_pipelines.geojson', name="Proposed gas pipelines", style_function= lambda feature: {
        'color': 'orange', 
    },tooltip=folium.GeoJsonTooltip(fields=['NAME', 'FEATURE_TYPE'])).add_to(m)

folium.GeoJson(data='../data/proposed_oil_pipelines.geojson', name="Proposed oil pipelines", style_function=lambda feature: {
        'color': 'red', 'dashArray': '5, 5'
    }, tooltip=folium.GeoJsonTooltip(fields=['NAME', 'FEATURE_TYPE'])).add_to(m)

folium.LayerControl(collapsed=False).add_to(m)
m.save("../html/proposed_pipelines.html")
