#!/usr/bin/env python

class SoldierGame(object):

	soldier_health = [] 
	soldier_class = []
	soldier_attack = [] 

	"""
	def add_soldier(self, _health, _class, _attack):
		soldier_health.append(100)
		soldier_class.append(0)
		soldier_attack.append(0)
	"""

	def addSoldier(self, soldier_instance):
		self.soldier_health.append(soldier_instance.health_stat)
		#self.soldier_class.append(soldier_instance.soldier_class)

	def printAll(self):
		for i in self.soldier_health:
			print i

class Soldier(object):

    health_stat = 100

    def __init__(self, uid, team):
        self.uid = uid
        self.team = team
        self.attack_stat = 0


    def attack(self, enemy):
        if self.team != enemy.team:
            enemy.health_stat = enemy.health_stat - self.attack_stat

    def print_status(self):
        print "ID:", self.uid
        print "Team:", self.team
        print "Health:", self.health_stat
        #print "Attack:", self.attack_stat


class Grenadier(Soldier):

    def __init__(self, uid, team):
        Soldier.__init__(self, uid, team)
        self.attack_stat = 30
        self.health_stat = 100

class Heavy(Soldier):
    def __init__(self, uid, team):
        Soldier.__init__(self, uid, team)
        self.attack_stat = 50
        self.health = 200

# start new game
newGame = SoldierGame()
ally_grenadier_1 = Grenadier(1, "Blue")
ally_heavy_2 = Heavy(2, "Blue")
enemy_grenadier_1 = Grenadier(3, "Red")

soldiers = [ally_grenadier_1, ally_heavy_2, enemy_grenadier_1]

for soldier in soldiers:
	newGame.addSoldier(soldier)


newGame.printAll()
