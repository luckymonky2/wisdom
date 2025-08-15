import random


number = random.randint(1, 100)
while True:
    try:
       guess = int(input('guess what number i have ! (1_100): ').lower())

       if guess < number :
           print('too low! guess another' )
       elif guess > number:
           print('too high! guess another')
       else:
           print("well done! you get the number ")
           break
    except ValueError:
        print('invalid! guess between (1_100) ')

