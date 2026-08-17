#Assume you are given an integer N between 0 and 1000 so 0<= N <=1000  . Write a piece of Python code that uses bisection search to guess N. The code prints two lines: 
# count: with how many guesses it took to find N,
#  and answer: with the value of N. Hints: If the halfway value is exactly in between two integers, choose the smaller one.

import random 
value = random.randint(0,1000)
value=300

low = 0
high = 1000
midpoint = (high + low)/2.0
numb_guess = 0 
espilon = 0.001
while abs(midpoint-value) >= espilon:
    numb_guess +=1
    if midpoint > value:
        high = midpoint
    else:
        low = midpoint
    midpoint = (high + low)/2.0
print(f"The  vaule was {value} and my guess was {numb_guess} \n and my vaule guess was {midpoint}")


# low = 0
# high = 1001
# guess = (high+low)//2
# count = 1
# while guess != value:
#  if guess < value:
#     low = guess
#  elif guess > value:
#   high = guess
#  guess = (high+low)//2
#  count += 1
# print("count:",count)
# print("answer:",guess)