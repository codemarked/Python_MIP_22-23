print('Start by entering float numbers')
print('This application returns:')
print('- The average value of numbers entered')
print('- The average difference between inputs')
print('- The highest and lowest number entered')
print()

lowestNumber = -1.0 # Lowest number storage
highestNumber = -1.0 # Highest number storage
totalNumbers = 0.0 # Total number values storage
totalRecords = 0 # Number of inputs
lastNumber = 0.0 # Last number input
averageNumberDifference = 0.0 # Average difference between number inputs

while True:
	inputstr = input(f'Enter number #{totalRecords+1}: ')
	if inputstr is '':
		break
	number = float(inputstr)
	if number == 0.0:
		break
	elif number is not 0.0:
		if highestNumber == -1.0 or number > highestNumber:
			highestNumber = number # Updating the highest number
		if lowestNumber == -1.0 or number < lowestNumber:
			lowestNumber = number # Updating the lowest number
		totalNumbers += number # Updating the total number values
		totalRecords += 1 # Incrementing the number of records
		numberDifference = abs(lastNumber - number) # Calculating the difference between the last stored number and the current number
		if lastNumber is not 0.0:
			if averageNumberDifference is 0.0:
				averageNumberDifference = numberDifference # Initializing number difference
			averageNumberDifference += numberDifference # Updating average
			averageNumberDifference /= 2.0			# number difference
		lastNumber = number # Updating the last number

if totalRecords == 0: # Fail safe method
	exit('Not enough records!')

print()

averageNumber = totalNumbers / totalRecords;

print('Average number:')
print(format(averageNumber,'.2f'))  # Average number

print('Average input difference:')
print(format(averageNumberDifference,'.2f')) # Average number input difference

print('Highest number:')
print(format(highestNumber,'.2f')) # Highest number

print('Lowest number:')
print(format(lowestNumber,'.2f')) # Lowest number
