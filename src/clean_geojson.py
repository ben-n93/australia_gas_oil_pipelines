import json

# Base dictionary for new Geojson files.
new_geojson = {"type" : "FeatureCollection", "name" : ""}

# Create new oil Geojson files.
with open('../data/Oil_Pipelines_v3.geojson') as f:
    data = json.load(f)
    built_oil_pipelines = []
    proposed_oil_pipelines = []
    for pipeline in data['features']:
        if pipeline['properties']['FEATURE_TYPE'] == 'Proposed Oil pipeline':
            proposed_oil_pipelines.append(pipeline)
        elif pipeline['properties']['FEATURE_TYPE'] == 'Oil pipeline':
            built_oil_pipelines.append(pipeline)

new_geojson['name'] = 'built_oil_pipelines'
new_geojson['features'] = built_oil_pipelines
with open('../data/existing_oil_pipelines.geojson', 'w') as f:
    json.dump(new_geojson, f)

new_geojson['name'] = 'proposed_oil_pipelines'
new_geojson['features'] = proposed_oil_pipelines
with open('../data/proposed_oil_pipelines.geojson', 'w') as f:
    json.dump(new_geojson, f)

# Create new gas Geojson files.
with open('../data/Gas_Pipelines_v3.geojson') as f:
    data = json.load(f)
    built_gas_pipelines = []
    proposed_gas_pipelines = []
    for pipeline in data['features']:
        if pipeline['properties']['FEATURE_TYPE'] == 'Proposed Gas pipeline':
            proposed_gas_pipelines.append(pipeline)
        elif pipeline['properties']['FEATURE_TYPE'] == 'Gas pipeline':
            built_gas_pipelines.append(pipeline)

new_geojson['name'] = 'built_gas_pipelines'
new_geojson['features'] = built_gas_pipelines
with open('../data/existing_gas_pipelines.geojson', 'w') as f:
    json.dump(new_geojson, f)

new_geojson['name'] = 'proposed_gas_pipelines'
new_geojson['features'] = proposed_gas_pipelines
with open('../data/proposed_gas_pipelines.geojson', 'w') as f:
    json.dump(new_geojson, f)
