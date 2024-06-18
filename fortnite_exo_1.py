""" Docstring 
    @author: 
    @File: 
    @Description: 
"""

def main(): 
    pass 

    # Variables (int, float, str)
    player_name = "Haven"
    ally_name = "Jonesy"
    player_life = 100
    player_armor = 125.55

    player_car = str('Ferrari')
    player_magic_points = 584.54
    player_distance = float(125)


    # Print (Method 1)
    player_type = "Monster" 
    print(f"{player_type} name: " + player_name)
    print(f"{player_type} life: " + str(player_life) + "\nPlayer Amror" + str(player_armor))

    # Print (Method 2 - Format String)
    print(f"Ally name: {ally_name} \nPlayer distance: {player_distance * 15}")

    # Input
    user_name = input("Please enter your name: ")
    print(f"Your name is: {user_name}")

# Main Guard 
if __name__ == "__main__": 
    pass 
    main()