#!/usr/bin/env python3

from PIL import Image # this library is for displaying images

print('Hi this is Hami first game building with python3')

response = input('Let\'s get started amigo! You ready? (yes/no): ').lower().strip()
score = 0
total_q = 5
odd_numbers= ['1', '3', '5', '7', '9'] # list of odd numbers

# Pictures to be displayed in a new window make sure you replace these pictures with pictures that are saved in your directory as this code in order for this to work
fail = Image.open('fail.jpg')
ok5 = Image.open('joy5.jpg')
joy4 = Image.open('joy4.jpg')
trump = Image.open('trump.jpg')
im = Image.open("kiriku.jpg")

if response.lower() == 'yes':

    attempts = 0
    while True: # keep looping until we either break out or exit() the program 
        response = input('1. Between plane and wind, which travels faster? ').lower().strip()
        if response.lower() == 'wind':
            score += 1
            print('\n You are right amigo for question #1!')
            break # exits the while loop
        else:
            print('\n Haoooch!! sorry amigo try again!')
            attempts += 1
            if attempts == 3:
                print(" Strike 3, you\'ve reach the limite.\n\n The answer was \"WIND\"\n\nPlease processed to the next quest!")
                break # Move on to the next 

    response = input('2. Who was the president of the USA in 2019? ').lower().strip()
    if response == 'trump' or response == 'donald' or response == 'donald trump':
        score += 1
        print('\n You are right amigo for question #2!')
        trump.show()
           
    else:
        print('\n Hooouu sorry amigo but nice second try!')
        fail.show()

    response = input('3. Fill in the blank: 7 * = 35? ')
    if response == '5':
        score += 1
        print('\n You got math skills amigo!')
    else:
        print('\n My friend you really need to work on your math!')
        

    response = input('4. From 1 to 10, give me one odd number? ')
    if response in odd_numbers:
        score += 1
        print('\n Well play amigo! Well play')
        joy4.show()
        
    else:
        print('\n That\'s an even number my friend. Try again next time!')
        fail.show()
        
    response = input('5. How do you check the current time? ').lower().strip()
    if response == 'clock'or response == 'watch':
        score += 1
        print('\n You are right amigo about that!')
        ok5.show()
      
    else:
        print('\n Not correct')
        fail.show()
        
    print('\n Alrigt my friend!!!! This is the end of our litle game.\n\n You scored', score, "out of 5 questions")
    grade = (score/total_q) * 100
    print("\n Your grade is:", str(grade) + '%')
print('\n Enjoy your day amigo.\n\nANY QUESTION AT THIS TIME?')

#show image
im.show()

