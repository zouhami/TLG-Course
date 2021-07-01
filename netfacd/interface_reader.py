#!/usr/bin/env python3
import netifaces
print(netifaces.interfaces())

## Hami  This will perform an additional fuction-Hami

for i in netifaces.interfaces():
    print('\n**************Details of Interface - ' + i + ' *********************')
    print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])

