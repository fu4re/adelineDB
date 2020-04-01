from init.Person import Person

class Manager(Person):

    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, 'manager')
        

    def giveRaise(self, precent, bonus = 0.1):
        Person.giveRaise(self, precent + bonus)

