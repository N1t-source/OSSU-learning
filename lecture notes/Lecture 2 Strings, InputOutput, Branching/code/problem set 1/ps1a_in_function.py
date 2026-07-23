def part_a(yearly_salary, portion_saved, cost_of_dream_home):
	#########################################################################
	
	portion_down_payment = 0.25
	down_payment_goal = cost_of_dream_home * portion_down_payment
	
	current_savings = 0.0
	r = 0.05  
	months = 0
	
	monthly_salary = yearly_salary / 12
	monthly_savings = monthly_salary * portion_saved
	
	###############################################################################################
	## Determine how many months it would take to get the down payment for your dream home below ## 
	###############################################################################################
	
	while current_savings < down_payment_goal:
	    current_savings += current_savings * (r / 12)
	    current_savings += monthly_savings
	    months += 1
	
	print(f"Number of months: {months}")
	return months