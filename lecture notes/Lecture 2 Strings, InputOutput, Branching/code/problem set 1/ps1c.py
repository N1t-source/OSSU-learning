## 6.100A PSet 1: Part C
## Name:
## Time Spent:
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

def edge_cases(initial_deposit, months, down_payment_cost):
    savings_high = initial_deposit * (1 + (high / 12)) ** months
    if savings_high < down_payment_cost:
        return 'Impossible'

    savings_low = initial_deposit * (1 + (low / 12)) ** months
    if savings_low >= down_payment_cost:
        return 'already'

    return "start"
response = edge_cases(initial_deposit, months, down_payment_cost)

if response == 'start':
  while (high - low) > 0.0000001:
    savings = initial_deposit * (1 + (r/12))**months

    if abs(savings - down_payment_cost) <= 100:
      break
    elif savings > down_payment_cost :
      high = r
      r = (low + high) / 2
      steps += 1
    else:
      low = r
      r = (low + high) / 2
      steps += 1
  print(f'Best savings rate :{r}')
  print(f'Bisection search steps :{steps}')
elif response == "Impossible":
   print(response)
else:
   print(response)
   
