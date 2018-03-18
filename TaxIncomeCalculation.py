def taxincome():
	taxincome = int(input("What's your taxable income?"))
	if taxincome <= 18200:
		print ("Your income after tax is: ${}".format(taxincome - 0))
	elif 18201 <= taxincome <= 37000:
		print ("Your income after tax is: ${}".format(taxincome - ((taxincome - 18200) * 0.19)))
	elif 37001 <= taxincome <= 87000:
		print ("Your income after tax is: ${}".format((taxincome - 3572) - ((taxincome - 37000)* 0.325)))
	elif 87001 <= taxincome <= 180000:
		print ("Your income after tax is: ${}".format((taxincome - 19822) - ((taxincome - 87000) * 0.37)))
	elif taxincome >= 180001:
		print ("Your income after tax is: ${}".format((taxincome - 54232) - ((taxincome - 180000) * 0.45)))
	else:
		print("No idea mate, dev has no idea what he's doing")

taxincome()