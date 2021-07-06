#!/usr/bin/env python3
import requests

## Define APOD 
apodurl = 'https://api.nasa.gov/planetary/apod?'
mykey = 'api_key=PAfHUOppaRFTi5mevR2XWpfAHqL6Zr5wZsTc9lq7'    ## your key goes in place of DEMO_KEY

## Call the webservice
apodurlobj = requests.get(apodurl + mykey)

## read the file-like object
apodread = apodurlobj.json()

## display our Pythonic data
print("\n\nConverted Python data")
print(apodread)

