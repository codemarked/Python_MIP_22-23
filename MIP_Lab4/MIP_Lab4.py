import random
import math

totalChances = 0.0
chances = []
items = []

# Add item to TreeList
def addItem(weight, item):
	global totalChances

	totalChances += weight
	chances.append(totalChances)
	items.append(item)

	print(f"Added » Item: {item}, Chance: {weight}, Index: {len(chances) - 1}")

	if len(chances) > 1:
		sort()

# Get random item from TreeList		
def get():
	global totalChances
	selected = float(totalChances * random.uniform(0, 1))
	print(f"Random Number Generated: {selected}")
	
	lowest = -1
	diff = -1
	for i in range(len(chances)):
		if lowest == -1:
			lowest = i
			diff = abs(chances[i] - selected)
			continue
		if chances[i] - selected < diff:
			lowest = i
			diff = abs(chances[i] - selected)
	return lowest;

# Sort TreeList
def sort():
	# Bubble sort | Start
	changed = True
	k = 1
	while changed:
		changed = False
		for i in range(len(chances) - k):
			if chances[i] > chances[i + 1]:
				(chances[i], chances[i + 1]) = (chances[i + 1], chances[i])
				(items[i], items[i + 1]) = (items[i + 1], items[i])
				changed = True
			++k
	# Bubble sort | End

# Init TreeList
def init(): # Aruncarea unui zar
	addItem(0.0, 0)
	addItem(0.3, 1)
	addItem(0.3, 2)
	addItem(0.3, 3)
	addItem(0.3, 4)
	addItem(0.3, 5)
	addItem(0.3, 6)
	
print("WeightedTreeList Implementation - Python")
print()
print("Initializing TreeList:")

init()

print()
print("Viewing sorted TreeList:")
for i in range(len(chances)):
	print(i, chances[i], items[i])
print()
print(f"Total Weight: {totalChances}")
print()

finished = False
while finished is False:
	finished = input() is None
	idx = get()
	print()
	print("Resulted:")
	print(f"- Item: {round(items[idx], 2)}")
	print(f"- Index: {chances[idx]} / {totalChances}")