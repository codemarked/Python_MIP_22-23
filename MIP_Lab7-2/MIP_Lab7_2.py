import mysql.connector as sql
import tkinter as tk
import numpy as np
from tkinter import *

database = sql.connect(host = "localhost",user = "project",password = "1234",database = "MIP_Lab")
# MYSQL
MX = 800
MY = 800

AX = 50
BX = MX - AX
AY = 50
BY = MY - AY

def TX(x):
	return max(min(AX + x, BX), AX)
def TY(y):
	return max(min(MY - y, BY), AY)

root = tk.Tk()

f = Frame(root)
f.pack(side = RIGHT)

c = Canvas(root, bg="white", width=MX,height=MY)
c.pack(side = LEFT)

def Draw():
	sqlcmd = database.cursor()
	sqlcmd.execute("SELECT * FROM records")

	result = sqlcmd.fetchall()
	
	records = []
	
	for x in result:
		records.append(int(x[0]))

	c.create_line(TX(0),TY(0), TX(MX),TY(0))
	c.create_text(TX(0), TY(0) + 20, text = 0, fill = "red", font=('Helvetica 15'))

	c.create_line(TX(0),TY(0), TX(0),TY(MY))
	c.create_text(TX(0) - 20, TY(0), text = 0, fill = "blue", font=('Helvetica 15'))

	if (len(records) == 0):
		return
	
	deviation = np.mean(records) # Find average speed - MACHINE LEARNING

	CLast = (TX(0),TY(records[0] * 5))
	for i in range(1, len(records)):
		x = TX(i * 50)
		y = TY(records[i] * 5)
		c.create_rectangle(x, y, x + 5, y + 5)

		c.create_rectangle(x, TY(0), x + 5, TY(0) + 5)
		c.create_rectangle(TX(0), x, TX(0) + 5, x + 5)

		c.create_text(x, TY(0) + 20, text = i, fill = "red", font=('Helvetica 15')) #X
		c.create_text(TX(0) - 20, TY(x), text = i * 10, fill = "blue", font=('Helvetica 15')) #Y
		c.create_line(x,AY,x,BY)
		c.create_line(AX,x,BX,x)
		c.create_line(CLast[0],CLast[1],x,y,fill = "green")
		CLast = (x,y)

	c.create_line(TX(0),TY(records[0] * 5),TX((len(records) - 1) * 50), TY(deviation * 5), fill = "purple")

def Table():
	sqlcmd = database.cursor()
	sqlcmd.execute("CREATE TABLE IF NOT EXISTS records (speed int(3))")

b1 = Button(f, text="Create Table", fg="red", command = Table)
b1.pack( side = TOP)

def Insert():
	sqlcmd = database.cursor()
	values = [(int(55),),(int(58),),(int(63),),(int(78),),(int(67),),(int(88),),(int(95),),(int(75),),(int(81),),(int(93),),(int(106),),(int(75),)]
	sqlcmd.executemany("""INSERT INTO records VALUES (%s)""", values)
	database.commit()

b2 = Button(f, text="Insert Default", fg="red",command = Insert)
b2.pack( side = TOP)

def Delete():
	sqlcmd = database.cursor()
	sqlcmd.execute("DELETE FROM records")
	database.commit()

b3 = Button(f, text="Delete All", fg="red",command = Delete)
b3.pack( side = TOP)

b4 = Button(f, text="Draw", fg="red", command = Draw)
b4.pack( side = TOP)

def Clear():
	c.delete("all")

b5 = Button(f, text="Clear", fg="red", command = Clear)
b5.pack( side = TOP)

root.mainloop()