from objects import*
import time
import random as r

world = World()

world.addPlayer(Player("John", Location(r.randrange(100), r.randrange(100), r.randrange(100))))
world.addPlayer(Player("George", Location(r.randrange(100), r.randrange(100), r.randrange(100))))
world.addPlayer(Player("Fin", Location(r.randrange(100), r.randrange(100), r.randrange(100))))

while (True):
	world.tick()
	time.sleep(1) # 0.05
