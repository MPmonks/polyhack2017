#PARSE THROUGH .ics FILE AND SAVE EVENT INFORMATION

$ pip install ics
>>> from ics import Calendar, Event
>>> c = Calendar()
>>> e = Event()
>>> e.name = "My cool event"
>>> e.begin = '20140101 00:00:00'
>>> c.events.append(e)
>>> c.events
[<Event 'My cool event' begin:2014-01-01 00:00:00 end:2014-01-01 00:00:01>]
>>> with open('my.ics', 'w') as my_file:
>>>     my_file.writelines(c)
>>> # and it's done !
