## 6.100A PSet 1: Part B
## Name:
## Time Spent:
## Collaborators:

##########################################################################################
## Get user input for yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise below ##
##########################################################################################
yearly_salary = int(input('Enter your salary:'))
protion_saved = float(
  input('Enter the percentage your of salary to save, as decimal:'))
cost_of_dream_home = float(
  input('Enter the cost of your dream house:'))
semi_annual_raise = float(input('Enter your semi annual raise \n percentage:'))
#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

amount_saved = 0
r = 0.05
monthly_deposit = (yearly_salary/12) * protion_saved
amount_saved += monthly_deposit
portion_down_payment = 0.25
down_payment =  cost_of_dream_home * portion_down_payment
semi_pay_raise = (yearly_salary * semi_annual_raise) /12


months = 0

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################

while amount_saved <= down_payment:
  amount_saved += amount_saved * (r/12)
  amount_saved += monthly_deposit
  months +=1
  if months % 6 == 0 and amount_saved <= down_payment:
    monthly_deposit_temp = (yearly_salary + semi_pay_raise) /12
    amount_saved += amount_saved * (r/12)
    amount_saved += monthly_deposit_temp


# 
    

print(f'Amount of months: {months}') 
