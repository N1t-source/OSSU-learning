# write code to do bisection search to find the cube root of the positive cubes 
# within some epsilon  Start with 

cube = -1
epsilon = 0.01
low = 0
high =cube 

numb_guess= 0 
midpoint = (high + low)/ 2.0

if cube < 0:
    is_negative = True
    cube = abs(cube)
    high =abs(cube) 
    midpoint = (high + low)/ 2.0
else:
    is_negative = False

while abs(midpoint**3 - cube) >= epsilon:
    numb_guess += 1
    if (midpoint**3) > cube :
        high = midpoint
    else:
        low = midpoint
    midpoint = (high + low)/ 2.0
if is_negative:
  print(f"-{midpoint} is closer to -{cube}\n took {numb_guess} guesses ")
else:
    print(f"{midpoint} is closer to {cube}\n took {numb_guess} guesses ")