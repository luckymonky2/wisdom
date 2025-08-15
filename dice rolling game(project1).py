import random


while True:
   choice = input('enter the value to roll the die (y/n): ' ).lower()
   if choice == 'y':
      diy1 = random.randint(1, 6)
      diy2 = random.randint(7, 9)
      print(f'({diy1}, {diy2}')
   elif choice == 'n':
       print('thank you for playing ')
       break
   else:
       print('error! enter the correct choice')
       
