import sys
import datetime
from eventClass import Event

<<<<<<< HEAD
def main():

	choice = ""
	choice = takeUserChoices()

	if choice == "google"
		importFromGoogle()
	else if choice == "ICS"
		importFromICS()

=======
def newEventInfo():
    num_events = input() # number of new events to add to calendar
    if num_events < 0:
        num_events = 0 # reset at 0 if poor input
    
    names = [] # list of event names
    estTimes = [] # list of estimated times needed for event completion
    deadlines = [] # list of event deadlines
>>>>>>> 16d176369dd861f6472ed9326f2d01adf4dfc498

    for i in range(0, num_events): # store event info from user input
        names.append(raw_input("enter event name: "))
        estTimes.append(input("enter estimated time to completion: "))
        deadlines.append(input("enter deadline: "))
    
    userEvents = [] # store new events data in list
    for i in range(0, num_events):
        userEvents.append({"name": names[i], "estTime": estTimes[i], "deadline": deadlines[i]})


# finds out what type of imput the user is taking
def takeUserChoices():
    class Task:
        def __init__(self, name):
            self.name = name
        def __init__(self, timeAllotted):
            self.timeAllotted = timeAllotted
        def __init__(self, deadlines):
            self.deadlines = deadline

    

# takes in the information if they choose to use google calendar as a source
def importFromGoogle():

# takes in the information from a ics file
def importFromICS():

if __name__ == '__main__':
	main()
