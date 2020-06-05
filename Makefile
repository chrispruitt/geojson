FILE_NAME=$(STATE_CODE)-county-fips.json

add:
	pbpaste > topojson/${FILE_NAME}
	topo2geo topojson/${FILE_NAME} geojson/${FILE_NAME}