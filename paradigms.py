

# Imperative Paradigm
number_of_apples = 56
user_name = "Jonesy"
user_age = 18
if (user_age <= 18): 
    print("")
elif (user_age > 18 and user_age < 25): 
    print("")
else: 
    print("")

# Procedural Paradigm 

def function_name (param_one, param_two): 
    pass 

# Function Definition 
def check_account (account_id: int, user_rights: str = "Admin") -> int : 
    print("Account id: " + str(account_id))
    print(f"Account id: {account_id}\nAccount sum: ") 

    def other_function (): 
        pass 

    if (user_rights == "Admin"): 
        return 645
    else: 
        return 455155

# Function Call
check_account(4518, "User")
print("Account sum" + str(check_account()) )



# Object Oriented Paradigm

# Class definition
class Vehicle:
    # Attributes (Properties)

    # Methods (behaviors) -> constructor, classic methods, get/set

    # Constructor 
    def __init__ (self, 
                  color: str, 
                  wheels: int = 4, 
                  damage: int = 0, 
                  speed: int = 0) : 

        # Instance Attributes
        self.color = color
        self.wheels = wheels
        
        self.speed = 0
        self.damage = 0

    def accelerate (self): 
        self.speed += 20 

    def get_vehicle_info (self) -> None:
        print(f"Vehicle color: {self.color}")
        print(f"Vehicle wheels: {self.wheels}")
        print(f"Vehicle Damage: {self.damage}")

    def vehicle_destruction (self) -> None: 
        self.damage = 100
        print("Vehicle is destroyed")

    

# Object (Class instances)
car = Vehicle("Blue")
bus = Vehicle("Green", 6) 
bike = Vehicle(color="Black", wheels=2, speed=60)

# Functional Paradigm  
