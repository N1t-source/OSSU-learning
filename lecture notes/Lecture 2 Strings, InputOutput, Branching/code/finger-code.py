### Finger code 
## Assume you are given a variable named number (has a numerical value). Write a piece of Python code that prints out one of the following strings: 
# positive if the variable number is positive
# negative if the variable number is negative
# zero if the variable number is equal to zero

try:
  number = int(input('Enter any integer:'))
  if number > 0 :
    print('The number is positive')
  elif number < 0 :
    print('The number is positive')
  elif number == 0 :
    print('The number is equal to zero')


except ValueError:
  print('The number is not an integer')




