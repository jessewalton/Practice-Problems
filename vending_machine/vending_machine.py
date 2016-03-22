#!/usr/bin/var python

"""

AUTHOR: Jesse Walton

DESCRIPTION: Virtual vending machine with minimal functionality to test object
  oriented design principles 

"""

class Vending_Machine(object):
  'Virtual vending machine to demonstrate object oriented design principles'
  
  def __init__(self):
    self.input_amount = 0     # track cust. money deposited
    self.coin_bank = 0        # amount of collected money
    self.inventory = []       # hold inventory
    
  def insertMoney(self, amount):
    self.coin_bank += amount 


class Snack(object):
  'Virtual base class for vending machine snacks' 
  def __init__(self, name):
    self.cost = 0.00            
    self.name = name
  pass


class Soda(Snack):
  def __init__(self, name):
    Snack.__init__(self, name)
    self.cost = 0.50


class Chips(Snack):
  def __init__(self):
    self.cost = 0.75