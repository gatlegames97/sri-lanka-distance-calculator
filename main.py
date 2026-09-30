##################################
# Example Distance Calculator
# Aaron Brumwell
# September 28th, 2026n
# Purpose: Take the usere's position and display their distance to Sri Lanka
###################################

import math
from geopy.geocoders import Nominatim
from geopy.geocoders import get_geocoder_for_service

def geocode(geocoder, config, query):
    cls = get_geocoder_for_service(geocoder)
    geolocator = cls(**config)
    location = geolocator.geocode(query)
    return location.address



import contextlib

with contextlib.suppress(ImportError):
    from pyscript import window
    input = window.prompt

geolocator = Nominatim(user_agent="sri-lanka-calculator")
nom=Nominatim(domain='gatlegames97.github.io/bearblocks.github.io', scheme='https')

earth_circumference = 6371.2

address = input("Enter the address you are currently at: \n")

#location = nom.geocode(address)
location = geocode("nominatim", dict(user_agent="specify_your_app_name_here"), address)
#location = geolocator.geocode(address)
user_latitude = location.latitude
user_longitude = location.longitude



#user_latitude = float(input("Enter your latitude: \n"))
#user_longitude = float(input("Enter your longitude: \n"))


sri_lanka_latitude = 7.608085
sri_lanka_longitude =  80.704727

latitudes = [user_latitude, sri_lanka_latitude]
longitudes = [user_longitude, sri_lanka_longitude]

high_latitude = max(latitudes)
low_latitude = min(latitudes)

high_longitude = max(longitudes)
low_longitude = min(longitudes)


latitude_diff = abs(high_latitude - low_latitude)
longitude_diff = abs(high_longitude - low_longitude)


#print(f"The latitude difference is {latitude_diff}.")
#print(f"The longitude difference is {longitude_diff}.")

hav_lat_diff = (1- math.cos(math.radians(latitude_diff))) / 2

#print(f"hav({latitude_diff}) = {hav_lat_diff}")

hav_long_diff = (1 - math.cos(math.radians(longitude_diff))) / 2

#print(hav_long_diff)

hav_theta = hav_lat_diff + math.cos(math.radians(sri_lanka_latitude)) * math.cos(math.radians(user_latitude)) * hav_long_diff

#print(f"hav_theta = {hav_theta}")

theta = 2 * math.asin((math.sqrt(hav_theta)))

#print(f"The angle in radians is {theta}")

angle_in_deg = math.degrees(theta)

#print(f"The angle in degrees is {angle_in_deg}")

distance = theta * earth_circumference

print(f"Your distance from Sri Lanka is {round(distance)}km.")

