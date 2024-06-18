""" 
    @File: 
    @Author: 
    @Description: 
"""

# Python Standard Library Modules 
import random
import sys
import os

# from os import system

""" Docstring - Main Function """


def generate_random_element(random_list: list):
    random_list_total_elements = len(random_list) - 1
    random_number = random.randint(0, random_list_total_elements)

    return random_list[random_number]


def Main() -> int:
    # ------------------------------------
    #            VARIABLES 
    # ------------------------------------

    # None (void) Variable
    app_started = None

    # Boolean Variables
    is_alive = True
    has_key = False

    # Numeric Variables (int, float, complex)
    player_score = 5451
    player_life = 150.50
    complex_number = 3j

    high_score = int(545)
    player_armor = float(4515.415)

    # ------------------------------------
    #            DATA COLLECTION  
    # ------------------------------------
    # Collection = one "variable" that contains multiple variables
    # list = [] ordered ; mutable/ changeable ; duplicates OK
    # set = {} unordered ; mutable; NO Duplicates
    # tuple = () ordered ; not changeable; Duplicates OK
    # dict = { key : "value" }

    # List
    player_skins = ["Jonesy", "Peely", "Haven", "Jonesy", "Gabe"]
    # player_skins = list(("Jonesy", "Peely", "Haven", "Jonesy"))

    player_skins.append("Victoria")
    # print(player_skins.count("Peely"))
    player_skins.insert(0, "Test")
    # player_skins.clear()
    len(player_skins)

    # print(player_skins)
    # print(player_skins[2])

    # Set 
    player_weapons = {"gun", "shotgun", "grenade"}
    for weapon in player_weapons:
        # print(weapon)
        pass

        # Tuple
    player_allies = ("Ramirez", "Gabe")

    # Dictionary

    game_settings = {
        "Operating System": "Windows",
        "Screen Size": 1080
    }

    # Random Operation
    player_skins = ["Jonesy", "Peely", "Haven", "Jonesy", "Gabe"]
    player_cars = ["car", "Peely", "Haven", "Jonesy", "Gabe"]
    player_motorbikes = ["Jonesy", "Peely", "Haven", "Jonesy", "Gabe"]

    lists = [player_skins, player_cars, player_motorbikes]

    os.system('cls')
    for list in lists:
        print(generate_random_element(list))

    return 1


if __name__ == "__main__":
    Main()

# Main Function 

# Simple Variables (None, bool, int, float, str)

# Data Collection Variables (list, tuple, set, dict)

# One Condition

# Print

# Main Guard
