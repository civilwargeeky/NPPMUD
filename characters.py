#This file will have classes and functions for characters. Including the player.

class Character(object): #Example #Also class names are all upper case, not camelCase
  def __init__(self, hp):
    self.hp = hp
    
class Player(Character): #Example
  def __init__(self, hp):
    super.__init__(hp)
    self.inventory = {}
    
class EnemyNPC(Character): #Example
  def __init__(self, hp):
    super.__init__(hp)
    self.annoyingness = 9001