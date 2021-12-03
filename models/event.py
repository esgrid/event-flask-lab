

class Event:

    def __init__ (self, date, name, guests, room, description, recurring):
        self.date = date
        self.name = name
        self.guests = guests
        self.room = room
        self.description = description
        self.recurring = recurring