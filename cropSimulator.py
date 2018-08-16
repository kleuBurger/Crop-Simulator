# Crop Simulator

import random

class Crop(object):
    """A generic food crop"""
    # Constructor
    def __init__(self,growth_rate, light_need, water_need):

        # Attributes
        self._growth = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = "Seed"
        self._type = "Generic"

        # The attributes above are prefixed with a underscore to show that they are private
        # Shows they should not be accessed directly from outwith the class

    def needs(self):
        # Return a dictionary containing the light and water needs
        return {"light need": self._light_need, "water need": self._water_need}

    # Method to report and provide information on the current status of the crop
    def report(self):
        # return a dictionary containing the type, status , growth and days
        return {"type": self._type,"growth": self._growth, "status": self._status,"days gorwing": self._days_growing}

    def update_status(self):
        if self._growth > 15:
            self._status = "Old"
        elif self._growth > 10:
            self._status = "Mature"
        elif self._growth > 5:
            self._status = "Young"
        elif self._growth > 0:
            self._status = "Seedling"
        elif self._growth == 0:
            self._status = "Seed"

    def grow(self,light,water):
        if light >= self._light_need and water >= self._water_need:
            self._growth += self._growth_rate
        # Increment days growing
        self._days_growing += 1
        # Update the status
        self.update_status()


def auto_grow(crop, days):
    # Grow the crop
    for day in range(days):
        light = random.randint(1,10)
        water = random.randint(1,10)
        crop.grow(light,water)

def manual_grow(crop):
    # Get the light and water values
    valid = False
    while not valid:
        try:
            light = int(input("Please enter a light value (1-10): "))
            if 1 <= light <= 10:
                valid = True
            else:
                print("Value entered not valid - please enter a value between 1 and 10")
        except ValueError:
                print("Value entered not calid - please enter a value between 1 and 10")
    valid = False
    while not valid:
        try:
            water = int(input("please enter a water value (1-10"))
            if 1 <= water <= 10:
                valid = True
            else:
                print("Value entered not valid - please enter a value between 1 and 10")
        except ValueError:
                print("Value entered not calid - please enter a value between 1 and 10")
        # Grow the crop
        crop.grow(light,water)

def display_menue():
    print("1. Grow Manually over 1 day")
    print("2. Grow Automatically over 30 days")
    print("3. Report Status")
    print("0. Exit the program")
    print()
    print("Please select an option above")


def menue_choice():

    option_valid = False
    while not option_valid:
        try:
            choice = int(input("option selected: "))
            if 0 <= choice <= 4:
                option_valid = True
            else:
                print("please enter a valid option")
        except ValueError:
            print("please enter a valid option")
            return choice

def manage_crop(crop):
    print("This is the crop management program")
    print()
    noexit = True
    while noexit:
        display_menue()
        option = menue_choice()
        print()
        if option == 1:
            manual_grow(crop)
        elif option == 2:
            auto_grow(crop, 30)
            print()
        elif option == 3:
            print(crop.report())
            print()
        elif option == 0:
            noexit = False
            print()
            print("Thank you for using crop simulator")







def main():
    # instaniate the class
    new_crop = Crop(1,4,3)
    manage_crop(new_crop)

if __name__ == "__main__":
    main()