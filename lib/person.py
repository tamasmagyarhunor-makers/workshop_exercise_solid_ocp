from lib.house import House

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def try_open_door(self):
        return True
    
    def walk_through_door(self, house):
        if house.door_open_status == True:
            return 'Walk through the open door'
        else:
            return "Door is closed, you're gonna bang youe head!"