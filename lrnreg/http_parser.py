#!/usr/bin/env python3
import urllib.request
import re
print("Where should we search?")
url = input()
print("Great! So we'll try to open this url " + str(url) + " to search for the phrase:")
searchFor = input()
searchMe = urllib.request.urlopen(url).read().decode("utf-8")
if re.search(searchFor, searchMe):
    print("Found a match!")
else:
    print("No match!")

'''
## Searching with Regular Expressions
Lab Objective
The regular expression (re) library is one of the most useful tools in the standard library. Unlocked with import re, using this library requires a knowledge of Regular Expressions, as well as how to use the tools within re itself. In this lab, we'll scratch the surface of what is possible with regular expressions.

Suppose you throw a bunch of darts at a dart board. If they all hit bulls-eye, you are accurate and precise. Accuracy refers to the closeness of a measured value to a standard or known value. Precision refers to the closeness of two or more measurements to each other. If you weigh a given substance five times, and get 3.2 kg each time, then your measurement is very precise. However, if the substance actually weighs 5.0 kg, then your measurement is not very accurate.

For the uninitiated. Regular Expression (regex) is a standardized language that allows us to create search expressions. Regex is ALWAYS precise (it will always return exactly what you asked for), the problem is that it is only as accurate as your search expression.

Before starting this code, read about the re module.

https://docs.python.org/3/library/re.html
Procedure
Take a moment to clean up your remote Desktop. For now, close all other terminal spaces or windows you might have open.

Open a new terminal.

Create /home/student/mycode/lrnreg/.

student@beachhead:~/mycode/lrnreg$ mkdir -p ~/mycode/lrnreg

Move to /home/student/mycode/lrnreg/.

student@beachhead:~/mycode/lrnreg$ cd ~/mycode/lrnreg

Launch vim.

student@beachhead:~/mycode/lrnreg$ vim http_parser.py

Begin with a Python 3.x Shebang line.


#!/usr/bin/env python3
Great. Now add support for the urllib library.


import urllib.request
Fantastic. Next add support for the RegEx library.


import re
Skip a line to make the text for readable. On the next line, place the following statement.


print("Where should we search?")
Fantastic, now set url equal to input()


url = input()
Ask the user what to search for, and print the URL for the user.


print("Great! So we'll try to open this url " + str(url) + " to search for the phrase:")
Now we want to collect input for what to search for.


searchFor = input()
Fantastic. Now let's use the urllib library to parse the URL entered by the user.


searchMe = urllib.request.urlopen(url).read().decode("utf-8")
This next line is an if statement with a conditional that reads as follows, "If searchFor pattern matches searchMe string". If you want to know more about using re.search() then read about the re module here: https://docs.python.org/2/library/re.html


if re.search(searchFor, searchMe):
The above function will return a matchObject, which tests True, so the above conditional will execute code under it on a match. For now, let's indent 4 whitespaces, and print a simple message.


    print("Found a match!")
Outside of the if statement, code the else statement.


else:
Now indent 4 whitespaces, and print a no match message.


    print("No match!")
Save and exit.

Back at the terminal, update permissions.

student@beachhead:~/mycode/lrnreg$ chmod u+x http_parser.py

Run the program. If it runs, you should be able to enter a URL and a phrase to search on. Run a few positive and negative tests with the data provided below.

student@beachhead:~/mycode/lrnreg$ python3 http_parser.py

Project Gutenberg (http://www.gutenberg.org) has lots of free books available that are in the public domain (i.e. legally available). Run the script at least twice. We want a positive, and negative result. A few suggestions are below.

Positive Test:

URL: https://alta3.com
Phrase: Alta3
Negative Test

URL: https://www.gutenberg.org/files/345/345-h/345-h.htm
Phrase: vegetarian
Positive Test:

URL: http://www.gutenberg.org/files/98/98-0.txt
Phrase: It was the best of times
Negative Test

URL: https://bing.com
Phrase: google it
The completed solution is shown below:


#!/usr/bin/env python3
import urllib.request
import re

print("Where should we search?")
url = input()
print("Great! So we'll try to open this url " + str(url) + " to search for the phrase:")
searchFor = input()
searchMe = urllib.request.urlopen(url).read().decode("utf-8")

if re.search(searchFor, searchMe):
    print("Found a match!")
else:
    print("No match!")
CODE CUSTOMIZATION 01 - Make the program continue to accept search strings from the user until some kind of quit command is passed by the user.

CODE CUSTOMIZATION 02 - Return to the user how many matches appear on a page.

CODE CUSTOMIZATION 03 - Write a script that allows a user to pass several words as input. Determine how many lines within a given text contain (any combination) of the words input by the user.

CODE CUSTOMIZATION 04 - (DIFFICULT) - Write a script that allows a user to pass several words as input. Determine how many sentences within a given text contain (any combination) of the words input by the user.

If you're tracking your code in GitHub, issue the following commands:

cd ~/mycode
git add *
git commit -m "your commit message"
git push origin main
'''
