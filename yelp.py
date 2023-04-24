import urllib.request
import json 
import requests

APIKEY='kRmfuQMRMVioJ7TXkyCvb2G0Vhwi1guBxBgtKIimEi7lH2D2d5vPa5AM7KwxwJAkCO4OdeZsb1J0qA7EsrvwObhVCv-3ag54-8Plz-tyuADXaw3jA8WZL8X0oEBDZHYx'


MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MAPBOX_TOKEN='pk.eyJ1IjoibGx1MSIsImEiOiJjbGZ2bzBhNnYwN3diM2x0c2I2N21lejFqIn0.bcxBv8L3Dt77gayTgFlvWw'




def get_json(url:str):
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.

    """
    # f=urllib.request.urlopen(url)
    # response_text=f.read().decode('utf-8')
    # response_data=json.loads(response_text)
    # return (response_data)
    #  headers = {
    #     'Authorization': f'Bearer {APIKEY}',}
    response = requests.get(url)
    data = response.json()
    return data

print(get_json("https://api.yelp.com/v3/businesses/search?term=delis&latitude=37.786882&longitude=-122.399972"))

# def get_lat_long(place_name: str) -> tuple[str, str]:
#     """
#     Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

#     See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
#     """
#     url=f'https://api.mapbox.com/geocoding/v5/mapbox.places/{place_name}.json?access_token={MAPBOX_TOKEN}'
#     data=get_json(url)
#     lat_long=data['features'][0]['geometry']['coordinates']
#     lat_long_tup= (lat_long[1],lat_long[0])
#     return lat_long_tup




# def rest_results(KEYWORD:str, place_name:str):
#     """Returns list of nearby places to eat based on keyword and place name/address."""
#     coordinates_tuple=get_lat_long(place_name)
#     lat=coordinates_tuple[0]
#     long=coordinates_tuple[1]
#     url=f'https://api.yelp.com/v3/businesses/search?term={KEYWORD}&latitude={lat}&longitude={long}'
#     data=get_json(url)
#     print(data)

