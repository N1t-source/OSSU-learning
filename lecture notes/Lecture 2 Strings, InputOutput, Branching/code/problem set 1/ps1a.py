## 6.100A PSet 1: Part A
## Name: Othniel
## Time Spent: 1:09:06.11 
## Collaborators: none

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################

#request for users salary
yearly_salary = int(input('Enter your yearly salary:'))
protion_saved = float(
  input('Enter the percentage your of salary to save, as decimal:'))
cost_of_dream_home = float(
  input('Enter the cost of your dream house:'))


#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

amount_saved = 0
r = 0.05

monthly_deposit = (yearly_salary/12) * protion_saved
amount_saved += monthly_deposit
portion_down_payment = 0.25
down_payment =  cost_of_dream_home * portion_down_payment

months = 0

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################


while amount_saved <= down_payment :
  amount_saved += amount_saved * (r/12)
  amount_saved += monthly_deposit
  months +=1

print(f'Amount of months: {months +1 }')