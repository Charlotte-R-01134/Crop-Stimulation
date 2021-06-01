from wheatclass import *
from potatoclass import *


def displayCropMenu():
    print("\nWhich crop would you like to create?\n")
    print("1. Potato")
    print("2. Wheat")
    print("\nPlease select an option from the above menu")

def select_option():
    valid = False
    while not valid:
        try:
            choice = int(input("Option Selected: > "))
            if choice in (1,2):
                valid = True
            else:
                print("Please enter a valid option")
        except ValueError:
            print("Please select a valid option")
    return choice

def createCrop():
    displayCropMenu()
    choice = select_option()
    if choice == 1:
        newCrop = Potato()
    elif choice == 2:
        newCrop = Wheat()
    return newCrop

def main():
    newCrop = createCrop()
    manageCrop(newCrop)

if __name__ == "__main__":
    main()