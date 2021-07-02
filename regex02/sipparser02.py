#!/usr/bin/python3

# Python standard library
import re

def main():
    # open the networktrace (text format)
    with open('networktrace.txt') as trace:
        # loop across the text file
        for line in trace:
            # look for a line that begins with sip:+ followed by digits@IP:port
            conobj = re.search(r'sip:\+(\d+)@\[(.*)\]:?(\d+)?', line)
            if conobj:
                print(conobj.group())
                print("The phone number is...")
                print(conobj.group(1))
                print("The IPv6 is...")
                print(conobj.group(2))
                print("The port is...")
                print(conobj.group(3))
if __name__ == "__main__":
    main()


'''
Use RegEx to Search Text
Lab Objective
The objective of this lab is to practice writing RegEx expressions and learn to search for patterns within text. In this lab you'll write two scripts. In the first you'll learn to search through a network capture (SIP trace) and pull out key information you want using RegEx. Specifically, the phone number, IPv6 address, and port.

In the second script you'll prompt the user for a URL and then also a string (word or phrase). Your script will then parse the text on that URL for the user's string and return "Found a match :)" or "No match :("

Before starting this code, read about the re module.


- https://docs.python.org/3/library/re.html
Procedure
Start this lab by experimenting with regex pattern matching on https://regex101.com

Create a directory to work in.

student@bchd:~$ mkdir ~/mycode/regex02/

Move into the new directory, /home/student/mycode/regex02/

student@bchd:~$ cd ~/mycode/regex02

Our first search will be against a snippet from a SIP VoIP trace. One line in the trace is of considerable interest, and that is the contact header. The contact header contains the phone number, the user's IPv6 address, and port. Everything else in this header is 'extra' and can be dropped. Using RegEx, we can 'capture' just the information we're looking for. To start, we'll hardcode a string to search through into our script. After we have that working we'll read in network trace from our local system.

Create a new script we can use to search through our text.

student@bchd:~/mycode/regex02$ vim sipparser01.py

Copy and paste the following into your script.


#!/usr/bin/python3
""" RZFeeser | Alta3 Research
Learn to search strings of data with complex regex patterns
"""

# Python standard library
import re

def main():
    # hardcode the string we'll search through
    contact = "Contact: <sip:+17175664428@[2600:2304:9210:ec::2]:5060;eri-generated-at=10.172.0.132>"
    
    # parse out the contact string using our regex logic
    conobj = re.search(r'sip:\+(\d+)@\[(.*)\]:?(\d+)?', contact)
    
    # searches test True if they find a match
    # False if no match
    if conobj:
        # display the match
        print(conobj.group())
        
        # display the phone number (group 1)
        print("The phone number is...")
        print(conobj.group(1))
        
        # display the IPv6 (group 2)
        print("The IPv6 is...")
        print(conobj.group(2))
        
        # display the port (group 3)
        print("The port is...")
        print(conobj.group(3))

if __name__ == "__main__":
    main()
Save and exit with :wq

Run your script.

student@bchd:~/mycode/regex02$ python3 sipparser01.py

Great! Now let's rewrite that script so that it parses a snippet from a pcap file (a network trace). Download the trace now.

student@bchd:~/mycode/regex02$ wget https://static.alta3.com/files/networktrace.txt

Display the file you just downloaded.

student@bchd:~/mycode/regex02$ cat networktrace.txt

Create a new script that will perform the same search through a file.

student@bchd:~/mycode/regex02$ vim sipparser02.py

Copy and paste the following into your script.


#!/usr/bin/python3

# Python standard library
import re

def main():
    # open the networktrace (text format)
    with open('networktrace.txt') as trace:
        # loop across the text file
        for line in trace:
            # look for a line that begins with sip:+ followed by digits@IP:port
            conobj = re.search(r'sip:\+(\d+)@\[(.*)\]:?(\d+)?', line)
            if conobj:
                print(conobj.group())
                print("The phone number is...")
                print(conobj.group(1))
                print("The IPv6 is...")
                print(conobj.group(2))
                print("The port is...")
                print(conobj.group(3))
if __name__ == "__main__":
    main()
Save and exit with :wq

Run your script, it should still produce a user phone, assigned IPv6, and port.

student@bchd:~/mycode/regex02$ python3 sipparser02.py

If you're tracking your code in GitHub, issue the following commands:

cd ~/mycode
git add *
git commit -m "introduction to regex searching with python"
git push origin main
'''
