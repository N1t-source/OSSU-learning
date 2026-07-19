### Strings
## Concatenate
# b = ":"
# c = ")"
# s1 =b + 2*c
# print(s1)
# f = "a"
# g = "b"
# h = "3"
# s2 = (f+g)*int(h)
# print(s2)

# s ='abc'
# print(len(s))

### Slicing

# s ='abcdefgh'
# print(s[3:6])
# print(s[2:5])
# print(s[3:6:2])
# print(s[::-1])

### Printing 
# a = 'the'
# b = 3
# c = 'musketeers'
# print(a,b,c)

### Input

# text = input('Type anything:')
# print(5*text)
##without casting any input is stored as string
# num1 = input('type a number:')
# print(5*num1)

# num2 = input('type a number')
# print(5*num2)

## type casting
# num3 = int(input('Enter a number:'))
# print(5*num3)

### input
# text = input('Enter a verb:')
# print(f'i can {text} better than you!')
# print((text+' ')*5)

### F-string

# question = input('Enter anything:')
# print(f'{question} is a input')

### You try it 
##user guesses the secret number
# secret = 5
# guess = int(input('Try to guess the secret number:'))
# vaild = True if secret == guess else False
# print(vaild)


### Branching 
secret = 10
guess = int(input('Enter a number:'))

if guess < secret :
  print('Your guess is too low')
elif guess > secret :
  print('Your guess is too high')
else :
  print(f'Bingo Your guess {guess} is correct')