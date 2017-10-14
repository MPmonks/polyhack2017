import sys
import datetime
import json
import operator
from eventClass import calRange

def main():
    choice = ""
    choice = takeUserChoices()
    
    if choice is "google":
        importFromGoogle()
    elif choice is "ICS":
        importFromICS()
    
    print sortEvents(newEventInfo())

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
    return

# takes in the information from a ics file
def importFromICS():
    return

# convert json to list of tuples that store user's new event input
# params: none
# returns: list of tuples
def newEventInfo():
    # open & parse json, store in temporary list
    jsonData = open("event_data.json", "r")
    if jsonData.tell() is not 0:
        tempList = json.loads(jsonData)
        print tempList

    names = [] # list of event names
    estTimes = [] # list of estimated times needed for event completion
    deadlines = [] # list of event deadlines

    # store event info from user input
    for i in range(0, num_events):
        names.append(raw_input("enter event name: "))
        estTimes.append(input("enter estimated time to completion: "))
        deadlines.append(input("enter deadline: "))
    
    # store new events data in tuple
    userEvents = []
    for i in range(0, num_events):
        userEvents.append((names[i], estTimes[i], deadlines[i]))
    
    return userEvents

# sorts list of new events by deadline
# params: events list of tuples storing name, estimated time, deadline
# returns: sorted list
def sortEvents(userEvents):
    userEvents = sorted(userEvents, key=lambda event: event[2])
    return userEvents

# call main
if __name__ == '__main__':
    main()

