class House:
    def __init__(self):
        self.door_open_status = False

    def open_door(self, person):
        if person.try_open_door():
            self.door_open_status = True
            return "The door is OPEN"
        else:
            return "The door is CLOSED"