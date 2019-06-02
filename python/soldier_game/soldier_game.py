#!/usr/bin/env python

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

class Heavy(Soldier):
    def __init__(self, uid, team):
        Soldier.__init__(self, uid, team)
        self.attack_stat = 50

ally_grenadier = Grenadier(1, "Blue")
ally_heavy = Heavy(2, "Blue")

enemy_grenadier = Grenadier(3, "Red")


ally_grenadier.print_status()
ally_heavy.print_status()
enemy_grenadier.print_status()

print "\nAttack!\n"
ally_grenadier.attack(enemy_grenadier)
ally_heavy.attack(enemy_grenadier)


ally_grenadier.print_status()
enemy_grenadier.print_status()

