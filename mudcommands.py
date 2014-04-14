#Experiment with Git. Round 2.
#Test file for directions.

import levels
import characters

def executecommand(command, currentRoom):
	if command == 'w':
		west()
	elif command == 'e':
		east()
	elif command == 's':
		south()
	elif command == 'n':
		currentRoom = north()
	else:
		print("What's that??")


def directionexists(dir):
	if dir in currentRoom.exits():
		return True
	else:
		return False

def west():
	if(directionexists('W')):
		print("You moved west.")
	else:
		print("You cannot go that way.")

def east():
	if(directionexists('E')):
		print("You moved east.")
	else:
		print("You cannot go that way.")

def south():
	if(directionexists('S')):
		print("You moved south.")
	else:
		print("You cannot go that way.")

def north():
	if(directionexists('N')):
		print("You moved north.") # Something like this...
	else:
		print("You cannot go that way.")

currentRoom = Room('N')

state = 0 # For standing, sitting, sleeping or fighting.

command = input("Enter command: ")
while(command != 'exit'):
	hp = 100
	mv = 100
	executecommand(command, currentRoom)
	command = input("HP: %d || MV: %d || >" %(hp, mv))

