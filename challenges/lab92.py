#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests
import datetime
import reverse_geocoder as rg

URL= "http://api.open-notify.org/iss-now.json"
def main():
    resp= requests.get(URL).json()

    # SOLUTION TO PART 2
    lon= resp["iss_position"]["longitude"]
    lat= resp["iss_position"]["latitude"]
    date_time = datetime.datetime.fromtimestamp(resp["timestamp"])
    coords_tuple = (lat, lon)
    location = rg.search(coords_tuple, verbose=False)
    city = location[0]["name"]
    country = location[0]["cc"]
    print(f"""
    CURRENT LOCATION OF THE ISS:
    Timestampe: {date_time}
    Lon: {lon}
    Lat: {lat}
    City/Country: {city}, {country}
    """)

if __name__ == "__main__":
    main()


