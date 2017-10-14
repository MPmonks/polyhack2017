import sys
from eventClass import Event

def newEventInfo():
    num_events = input() # number of new events to add to calendar
    if num_events < 0:
        num_events = 0 # reset at 0 if poor input
    
    names = [] # list of event names
    estTimes = [] # list of estimated times needed for event completion
    deadlines = [] # list of event deadlines

for i in range(0, num_events): # store event info from user input
    names.append(raw_input("enter event name: "))
    estTimes.append(input("enter estimated time to completion: "))
    deadlines.append(input("enter deadline: "))
    
    userEvents = [] # store new events data in list
    for i in range(0, num_events):
        userEvents.append({"name": names[i], "estTime": estTimes[i], "deadline": deadlines[i]})

def main():

	raw_input(num_events)

	num_events = 0
	names[num_events]
	estTimes[num_events]
	deadlines[num_events]

	for i in num_events:
		names

	#userEvents[


if __name__ == '__main__':
	main()
