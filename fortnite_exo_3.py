# Python Classes Exo 3
import random


class Vehicle:

    def __init__(self, power: bool, door, speed: float, wheels: int = 4):
        # Instance attributes
        self.power = power
        self.door = door
        self.speed = speed
        self.wheels = wheels

    def start_engine(self):
        self.power = True
        print("\"Vrn vrn!!\" you rev your new cars engine \n You now travel faster")

    def accelerate(self):
        if (self.power == True):
            self.speed += 20


class Weapon:
    def __init__(self, name, damage, durability=random.randint(1, 20)):
        self.name = name
        self.damage = damage
        self.durability = durability

    def attack(self):
        if self.name != "fists":
            self.durability -= 1


class Character:

    def __init__(self, name, action=None, weapon=Weapon('fists', 5)):
        # Instance attributes
        self.name = name
        self.action = action
        self.weapon = weapon
        self.car = None

    def walking(self):
        self.action = "Walking"
        return (f"{self.name} is {self.action.lower}")

    def driving(self, car):
        self.action = "Driving"
        self.car = car
        self.car.start_engine()

    def attack(self):
        self.action = "Fighting"
        self.weapon.attack()
        if self.weapon.durability == 0:
            print(f"Your {self.weapon.name} is broken")
            self.weapon = Weapon('fists', 5)

        return f"{self.name} attacks the monster with their {self.weapon.name} for {self.weapon.damage}"


class Monster:
    def __init__(self):
        self.type = None
        self.health = None
        self.damage = None


class Encounter:
    def __init__(self):
        self.type = None
        self.content = None
        self.distance = None

    def getContentMessage(self):
        if type(self.content) == Weapon:
            return "A " + self.content.name
        elif type(self.content) == Character:
            return self.content.name + " is waiting for you with his " + self.content.weapon.name
        elif type(self.content) == Vehicle:
            return "A shiny new car"
        else:
            return "A " + self.content.type + " is growling at you"


def Main():
    car = Vehicle(False, 4, 0)
    car.start_engine()
    car.accelerate()

    Ramirez = Character("Ramirez", 30)
    Ramirez.walking()
    Ramirez.driving()


if __name__ == "__main__":
    Main()

# Main Function

# Two Classes (Vehicle class & Character class)

"""  Vehicle Class: 
    - Constructor with 3 instance attributes (power, doors, wheels)
    - Two methods: Start ; Accelerate 
"""
"""  Character Class: 
    - Constructor with 2 instance attributes (name, age)
        one mandatory parameter & one optional parameter
    - Two methods: Walking, Driving 
"""

# Class Instances

# Main Guard
