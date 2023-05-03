#!/usr/bin/python3


import requests


api_url = "https://randomuser.me/api"

response = requests.get(api_url)

info = response.json()

name = info["results"][0]["name"]

location = info["results"][0]["location"]



print("Name: "+name["first"]+" "+name["last"])

print("Location: "+location["street"]["name"]+" "+str(location["street"]["number"])+" "+location["city"]+" "+location["country"])
