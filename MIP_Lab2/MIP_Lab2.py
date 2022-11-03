# Initializing List
vector = list()

# Values input
a = 0
print('Start by adding numbers: ')
while True:
	inputvalue = input()
	if inputvalue is None:
		break
	number = int(inputvalue)
	if number == -1:
		break
	vector.append(number)
	++a

print(f'Initial vector: {vector}')

# Bubble sort | Start
changed = True
k = 1
while changed:
	changed = False
	for i in range(len(vector) - k):
		if vector[i] > vector[i + 1]:
			bubble = vector[i];
			vector[i] = vector[i + 1]
			vector[i + 1] = bubble
			changed = True
		++k
# Bubble sort | End
print(f'Final vector: {vector}')



