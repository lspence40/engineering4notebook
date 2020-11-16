def doMath(a, b, func):
	if func == 1:  # addition
		return a + b
	if func == 2:  # subtraction
		return a - b
	if func == 3:  # multiplication
		return a * b
	if func == 4:  # division
		return round(a / b, 2)
	if func == 5:  # modular division
		return a % b

a = 5
b = 7

print("Sum:\t\t" + str(doMath(a,b,1)))
print("Difference:\t" + str(doMath(a,b,2)))
print("Product:\t" + str(doMath(a,b,3)))
print("Quotient:\t" + str(doMath(a,b,4)))
print("Modulo:\t\t" + str(doMath(a,b,5)))
