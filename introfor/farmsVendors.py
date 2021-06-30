#!/usr/bin/env python3
# create a list of strings
vendors = ["hami", "cisco", "hami1", "juniper", "hami2", "big_ip", "f5", "arista", "alta3", "zach", "stuart"]
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

# create a second list of strings
approved_vendors = ["cisco", "juniper", "big_ip"]
realFarms = ["SE Farm", "NE Farm"]
print(farms)
for y in farms:
	print("\nI said the farms is " + y, end="")
	if y not in realFarms:
print(" - NOT IN THE LIST OF FARMS!", end="")
# loop across the list called vendors
for x in vendors:
    print("\nThe vendor is " + x, end="")   # newline, print current vendor, and end without newline
    if x not in approved_vendors:   # if x does not appear within the list approved_vendors
        print(" - NOT AN APPROVED VENDOR!", end="")
print("\nOur loop has ended.") # print when loop has finished
