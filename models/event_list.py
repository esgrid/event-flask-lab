from models.event import Event
from datetime import date

event1 = Event(date(2021, 12, 1), "Convivio Universidad", 10, "Meadows", "Convivio universitario", False)
event2 = Event(date(2021, 10, 20), "Special Talk", 5, "New College", "Special talk in New College", False)
event3 = Event(date(2021, 5, 17), "Science and Religion conference", 20, "Martin Hall", "Michael Fuller speaks on science and religion", True)

events = [event1, event2, event3]

def add_new_event(event):
    events.append(event)

def delete_event(id, current_events):
    if current_events != []:
        current_events.remove(current_events[id])