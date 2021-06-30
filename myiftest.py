#!/usr/bin/env python3

say = 'you are on time '
say2 = 'you are late'

# wrap connection in a float() to accept decimals as numbers
arrival = float(input("What is your connection speed in Mbps?"))

# if input value was higher or equal to 25
if arrival >= 25:
    message = say + ' and you are way head, thank buddy'
elif arrival >= 5:
    message = say + ' you are just on time buddy.'
elif arrival >= 2:
    message = say2 + ' you are less than 5 mintes, so you are late.'
else:
    message = say2 + ' you are very late, what happened?'
print(message)

