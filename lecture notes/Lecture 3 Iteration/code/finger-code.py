#Assume you are given a positive integer variable named N.
#  Write a piece of Python code that prints hello world on separate lines,
#  N times. You can use either a while loop or a for loop.

question = int(input("Enter a number to print 'Hello world' n times: "))
for i in range(1,(question +1)):
  print(f'\nHello world'*i)