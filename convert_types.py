import json

# TopoJson Format
# with open('initial.json') as json_file:
#     data = json.load(json_file)

#     for i, obj in enumerate(data['objects']['cb_2015_kentucky_county_20m']['geometries'], start=0):
#         data['objects']['cb_2015_kentucky_county_20m']['geometries'][i]['properties']['COUNTYFP'] = int(obj['properties']['COUNTYFP'])
#         data['objects']['cb_2015_kentucky_county_20m']['geometries'][i]['properties']['STATEFP'] = int(obj['properties']['STATEFP'])
#         data['objects']['cb_2015_kentucky_county_20m']['geometries'][i]['properties']['COUNTYNS'] = int(obj['properties']['COUNTYNS'])

#     with open('result.json', 'w') as fp:
#         json.dump(data, fp, separators=(',', ':'))

# GeoJson Format
with open('geojson/ky-county-fips.json') as json_file:
    data = json.load(json_file)

    for i, obj in enumerate(data['features'], start=0):
        data['features'][i]['properties']['COUNTYFP'] = int(obj['properties']['COUNTYFP'])

    with open('result.json', 'w') as fp:
        # output to json file and remove whitespace
        json.dump(data, fp, separators=(',', ':'))

