#Task 1
class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner
    def update_owner(self, new_owner):
        self.owner = new_owner
        
Vehicle1 = Vehicle(1001, 'GMC Acadia', 'Kevin Galler') 
Vehicle1.update_owner('Kent Smith')
print(f"New owner of {Vehicle1.type} has been changed to {Vehicle1.owner}.")

Vehicle2 = Vehicle(1002, 'Ford F-150', 'David Stevens')
Vehicle2.update_owner('Victor Brunson')
print(f"New owner of {Vehicle2.type} has been changed to {Vehicle2.owner}. ")

#Task 2
class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0
    def add_participant(self, name):
        self.name = name
        self.participant_count += 1
        print(f"{self.name} has been added to the Guest List.")
    def get_participant_count(self):
        print(f"The total number of guests is {self.participant_count}")
        return self.participant_count

event = Event('Donation Gala', 12/1/2025)
event.add_participant('Kevin')
event.add_participant('Jennifer')
event.add_participant('Yolanda')
event.add_participant('Brian')
event.get_participant_count()