# import requests
# def getLatLong(address):
#     data = {}
#     try:
#         key = 'AIzaSyBRowGYaywRZljVn9NZ-jv-MDhVNlEjuX4'
#         address_gmap = address.replace(" ", "+")
#         response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+address_gmap+'&key='+key).json()
#         if response.get('status') == ('OK'):
#             data['gmap'] = response.get('results')[0]
#         geolocator = Nominatim()
#         location = geolocator.geocode(address)
#         if location != None:
#             data['geopy'] = location.raw
#             data['latitude'] = str(location.latitude)
#             data['longitude'] = str(location.longitude)
#             geohash_name = geohash.encode(float(location.latitude), float(location.longitude), 7)
#             data['geohash'] = str(geohash_name)
#         else:
#             data['error'] = 'address invalid'
#     except Exception as e:
#         #print (e.message)
#         data['error'] = e.message
#     #print (data)
#     return data