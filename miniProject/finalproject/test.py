import requests

URL= "http://127.0.0.1:2224/" # I had the url incorrect earlier

print(requests.get(URL + "room").text)  # this path doesn't return json, just plaintext-- so must use .text instead of .json()
print(requests.get(URL + "map").json())
#print(requests.get("https://aux1-b860adc9-d1c5-41dd-ac6c-006ce875116d.live.alta3.com/map").json())
