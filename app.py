# single line commentary
# another single line comment

# Python Standard Library (PSL)
import random
import sys
import os
import math

from fortnite_exo_2 import generate_random_element
from fortnite_exo_3 import Character, Weapon, Encounter, Vehicle, Monster


class Game:
    def __init__(self):
        self.player_life = 100
        self.player_score = 0
        self.player_name = input("Type your character's name: ")
        self.player = Character(self.player_name)
        self.player_magic_points = 54.545
        self.treasure_distance = random.randint(10, 99)
        self.player_points = float(54)
        self.weapons = [Weapon("gun", 15), Weapon("sword", 25), Weapon("grenade", 45)]
        self.friendlies = [Character("Jonesy", "Walking", generate_random_element(self.weapons)),
                           Character("Peely", "Walking", generate_random_element(self.weapons)),
                           Character("Haven", "Walking", generate_random_element(self.weapons)),
                           Character("Jonesy", "Walking", generate_random_element(self.weapons)),
                           Character("Gabe", "Walking", generate_random_element(self.weapons))]
        self.allies = []
        self.welcome_sentence = "Welcome, dear " + self.player_name + "! Enjoy the \"game\"!"
        print(self.welcome_sentence)

    def createMonster(self):
        monster_points = random.randint(0, 100)
        monster = Monster()
        monster.damage = round(monster_points / 10)
        monster.health = monster_points
        if monster_points > 80:
            monster.type = "Big Monster"
        elif monster_points == 80:
            monster.type = "Regular Monster"
        elif monster_points > 60:
            monster.type = "Small Monster"
        else:
            monster_points += 10
            monster.type = "Baby Monster"
        return monster

    def fightLoop(self, monster):

        while monster.health > 0 and self.player_life > 0:
            print(self.player.attack())
            monster.health -= self.player.weapon.damage
            print(f"The monster still has {monster.health} health")
            if monster.health > 0:
                for ally in self.allies:
                    if monster.health > 0:
                        print(ally.attack())
                        monster.health -= ally.weapon.damage
                        print(f"The monster still has {monster.health} health")
            if monster.health > 0:
                print(f"The monster hits you for {monster.damage} you still have {self.player_life} health")
                self.player_life -= monster.damage
            else:
                print("You have slayed the monster")
                input()
                self.player_score += monster.damage * 10
            if self.player_life <= 0:
                print(f"GAME OVER\nYour score is {self.player_score}")

    def startEncounter(self, encounter):
        if self.player.car is None:
            self.treasure_distance -= encounter.distance
        else:
            self.treasure_distance -= encounter.distance * 2
        if encounter.type == "friendly":
            self.allies.append(encounter.content)
            self.friendlies.remove(encounter.content)
            print(encounter.content.name + " has joined your forces")
        elif encounter.type == "enemy":
            self.fightLoop(encounter.content)
        elif encounter.type == "loot":
            self.player.weapon = encounter.content
            print(f"You found a {encounter.content.name}!")
        else:
            self.player.driving(encounter.content)
        if self.treasure_distance <= 0 <= self.player_life:
            print("You have reached the treasure")
        else:
            print(f"You have {self.player_life} health and {self.treasure_distance}Km to walk")
    def gameLoop(self):
        encounter_types = ["friendly", "enemy", "loot", "car"]
        north_encounter = Encounter()
        west_encounter = Encounter()
        east_encounter = Encounter()

        while self.player_life > 0 and self.treasure_distance > 0:
            north_encounter.distance = random.randint(0, 100)
            west_encounter.distance = random.randint(0, 100)
            east_encounter.distance = random.randint(0, 100)
            for e in [north_encounter, west_encounter, east_encounter]:
                if len(self.friendlies) == 0 and "friendly" in encounter_types:
                    encounter_types.remove("friendly")
                encounter_type = generate_random_element(encounter_types)
                e.type = encounter_type
                if encounter_type == "friendly":
                    ally = generate_random_element(self.friendlies)
                    e.content = ally
                elif encounter_type == "enemy":
                    monster = self.createMonster()
                    e.content = monster

                elif encounter_type == "loot":
                    weapon = generate_random_element(self.weapons)
                    e.content = weapon

                elif encounter_type == "car":
                    e.content = Vehicle(False, 4, 0)
                    encounter_types.remove("car")
            north_str = f"North Road {north_encounter.distance}Km: {north_encounter.getContentMessage()}"
            west_str = f"West Road {west_encounter.distance}Km: {west_encounter.getContentMessage()}"
            east_str = f"East Road {east_encounter.distance}Km: {east_encounter.getContentMessage()}"

            print(f"""
                                                              {north_str}
                                                                  |
                                                                  |
                                                                  |
                          =================================== [You are here] ===================================
                           |                                                                                 |
                           |                                                                                 |
                        {west_str}                                     {east_str}
                           |                                                                                 |
                           |                                                                                 |
                      """)
            path = ""
            while path not in ["W", "N", "E", "w", "n", "e"]:
                path = input("Choose your path (W,N,E)")
            if path == "N" or path == "n":
                self.startEncounter(north_encounter)
            if path == "E" or path == "e":
                self.startEncounter(east_encounter)
            if path == "W" or path == "w":
                self.startEncounter(west_encounter)
        if self.treasure_distance <= 0 <= self.player_life:
            print(f"YOU WIN!\n Your score is {self.player_score}")

def main():
    replay = ""
    while replay != "N" and replay != "no" and replay != "No":
        game = Game()
        game.gameLoop()
        while replay != "N" and replay != "no" and replay != "No" and replay != "Y" and replay != "yes" and replay != "Yes":
            replay = input("Do you want to play again? Yes/No")


if __name__ == "__main__":
    main()
