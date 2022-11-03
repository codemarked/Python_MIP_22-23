# Base Currency
base_currency = 'RON'


# Compared to RON
currencies = []
values = []

# Lambda Divider Function
divider = lambda x, y: x / y
# Lambda Multiplier Function
multiplier = lambda x, y: x * y

# Main Conversion Function
def convert(from_name,from_value,to_name):
	global base_currency
	if base_currency != from_name.upper():
		# Using the lambda Divider Function
		from_value = divider(from_value, getValue(from_name))
		from_name = base_currency
		# Converting to the base currency
		
	# Using the lambda Multiplier Function
	return multiplier(from_value, getValue(to_name))


# Store Currency
def addCurrency(name, value):
	currencies.append(name)
	values.append(value)

	print(f"Added: {name} » {value}")

	if 1 < len(currencies):
		sort()


# Get Currency Index
def getIndex(name):
	for i in range(len(currencies)):
		if currencies[i] == name.upper():
			return i;
	return -1;

# Get Currency Value
def getValue(name):
	for i in range(len(currencies)):
		if currencies[i] == name.upper():
			return values[i];
	return -1;

# Sort Currency
def sort():
	# Bubble sort | Start
	changed = True
	k = 1
	while changed:
		changed = False
		for i in range(len(values) - k):
			if values[i] > values[i + 1]:
				(values[i], values[i + 1]) = (values[i + 1], values[i])
				(currencies[i], currencies[i + 1]) = (currencies[i + 1], currencies[i])
				changed = True
			++k
	# Bubble sort | End

# Init Currencies
def init(): # WorldWide Live Currency
	addCurrency('EUR', 4.90)
	addCurrency('USD', 5.02)
	addCurrency('CHF', 4.96)
	addCurrency('GBP', 5.66)
	addCurrency('JPY', 0.034)
	addCurrency('CAD', 3.65)
	
# Program | Start
print("Currency Converter Implementation - Python")
print()
print("Initializing Currency Storage:")
print()

# Initialize Currencies
init()

print()
print("Stored Currencies:")
print()
for i in range(len(currencies)):
	print(i, currencies[i], values[i])
print()
print(f"Start Converting: <From_Currency> <Value> <To_Currency>")
print()

# Handle Input
while True:
	input_text = input()
	if input_text is None:
		break
	input_data = input_text.split(' ')
	conversion = convert(input_data[2], float(input_data[1]), input_data[0])
	print()
	print(f"{input_data[0]} » {input_data[2]} | {input_data[1]} » {round(conversion, 2)}")

# Program | End