#This file will contain the classes and associated functions for getting information from rooms.
#It will also deal with events and things that happen in rooms.

import saving

def Room(object): #Example
  def __init__(self, stuff):
    if saving.exists(stuff):
      self = saving.load(stuff)