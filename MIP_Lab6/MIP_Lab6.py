import random
from utils import*

points_reader = open("storage/points.txt", "r") # File Read
points_data = points_reader.readlines()
points_reader.close()

circles_reader = open("storage/circles.txt", "r") # File Read
circles_data = circles_reader.readlines()
circles_reader.close()

data_writer = open("storage/output.txt", "w") # File Write
data_writer.truncate(0) # delete file contents

print()
data_writer.write("\n")
print("Points:")
data_writer.write("Points:\n")

lastPoint = None
for point_data in points_data:
	point = Point()
	try: # Exception Handle
		point.fromData(point_data)
	except:
		point.init(random.randrange(0,20),random.randrange(0,20))
	print(point)
	if lastPoint is not None:
		output = f"Dist({point}) and ({lastPoint}): {round(point.distance(lastPoint),2)}" # Distance
		print(output)
		data_writer.write(output + "\n")
	lastPoint = point
	print()


print()
data_writer.write("\n")
print("Circles:")
data_writer.write("Circles\n")

lastCircle = None

for circle_data in circles_data:
	circle = Circle()
	try: # Exception Handle
		circle.fromData(circle_data)
	except:
		circle.init(random.randrange(0,20),random.randrange(0,20),random.randrange(0,20))
	print(circle)
	output = f"Area({circle}): {round(circle.area(),2)}" # Area
	print(output)
	data_writer.write(output + "\n")
	if lastCircle is not None:
		output = f"Dist({point}) and ({lastCircle}): {round(circle.distance(lastCircle),2)}" # Distance
		print(output)
		data_writer.write(output + "\n")
	lastCircle = circle
	print()

data_writer.close()
