## 6.100A PSet 1: Part C
## Name:Othniel 
## Time Spent: 3:16:10.49
## Collaborators:

##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input('Enter the inital deposit:'))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
months =  36
cost_of_house = 800000
down_payment = 0.25

down_payment_cost = cost_of_house * down_payment

low = 0.0
high = 1.0
r = (low + high) / 2
steps = 0
savings = 0
##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################

def edge_cases(initial_deposit, months, down_payment_cost,low=0.0,high=1.0):
    # Check the upper bound first: if even saving with r = 1.0 is not enough,
    # there is no valid solution.
    savings_high = initial_deposit * (1 + (high / 12)) ** months
    if savings_high < down_payment_cost:
        return 'Impossible'

    # Check the lower bound next: if r = 0.0 already reaches the goal,
    # then the lowest rate is just 0.0.
    savings_low = initial_deposit * (1 + (low / 12)) ** months
    if savings_low >= down_payment_cost:
        return 'already'

    return "start"
response = edge_cases(initial_deposit, months, down_payment_cost)

if response == 'already':
  print(f'Best savings rate: 0')
  print(f'Bisection search steps :{steps}')
  
elif response == "Impossible":
   print(f'Best savings rate: None')
   print(f'Bisection search steps :{steps}')
else:
   # Bisection search: keep narrowing the range until it is small enough.
     while (high - low) > 0.0000001:
       steps += 1
       # Test the current midpoint rate.
       savings = initial_deposit * (1 + (r/12))**months
   
       # If the savings are close enough to the target, stop searching.
       if abs(savings - down_payment_cost) <= 100:
         break
       # If savings are too high, the target rate is lower than the midpoint.
       elif savings > down_payment_cost :
         high = r
         # Recompute the midpoint after shrinking the upper half.
         r = (low + high) / 2
       else:
         low = r
         # Recompute the midpoint after shrinking the lower half.
         r = (low + high) / 2
     print(f'Best savings rate: {round(r, 4)}')
     print(f'Bisection search steps :{steps}')