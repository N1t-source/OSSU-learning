def part_c(initial_deposit):
	#########################################################################
	##################################################################################################
	## Determine the lowest rate of return needed to get the down payment for your dream home below ##
	##################################################################################################
	months = 36
	cost_of_house = 800000
	portion_down_payment = 0.25
	down_payment_goal = cost_of_house * portion_down_payment

	low = 0.0
	high = 1.0
	steps = 0

	if initial_deposit * (1 + high / 12) ** months < down_payment_goal:
		return None, steps

	if initial_deposit * (1 + low / 12) ** months >= down_payment_goal:
		return 0.0, steps

	while True:
		r = (low + high) / 2
		steps += 1
		savings = initial_deposit * (1 + r / 12) ** months

		if abs(savings - down_payment_goal) <= 100:
			return r, steps
		elif savings > down_payment_goal:
			high = r
		else:
			low = r
