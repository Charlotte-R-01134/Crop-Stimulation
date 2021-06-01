import random

class Crop:
    def __init__(self, agrowthRate, alightNeed, awaterNeed):
        self.growth = 0
        self.daysGrowing = 0
        self.growthRate = agrowthRate
        self.lightNeed = alightNeed
        self.waterNeed = awaterNeed
        self.status = "Seed"
        self.type = "Generic"

    def needs(self):
        return {'light need': {self.lightNeed}, 'water need': {self.waterNeed}}
    
    def report(self):
        return {'type':self.type, 'status':self.status, 'growth':self.growth, 'days growing':self.daysGrowing}
    
    def updateStatus(self):
        if self.growth > 15:
            self.status = 'Old'
        elif self.growth > 10:
            self.status = "Mature"
        elif self.growth > 5:
            self.status = "Young"
        elif self.growth > 0:
            self.status = "Seedling"
        elif self.growth == 0:
            self.status = "Seed"
    
    def grow(self,light, water):
        if light >= self.lightNeed and water >= self.waterNeed:
            self.growth += self.growthRate
        self.daysGrowing += 1
        self.updateStatus()

def autoGrow(crop, days):
    for day in range(days):
        light = random.randint(1,10)
        water = random.randint(1,10)
        crop.grow(light, water)

def manualGrow(crop):
    valid = False
    while not valid:
        try:
            light = int(input("Please enter a light value (1-10): "))
            if 1 <= light <= 10:
                valid = True
            else:
                print("Value entered not valid - please enter a value between 1 and 10")
        except ValueError:
            print("Value entered not valid - please enter a value between 1 and 10")
    valid = False
    while not valid:
        try:
            water = int(input("Please enter a water value (1-10): "))
            if 1 <= water <= 10:
                valid = True
            else:
                print("Value entered not valid - please enter a value between 1 and 10")
        except ValueError:
            print("Value entered not valid - please enter a value between 1 and 10")
    crop.grow(light, water)

def displayMenu():
    print("1. Grow manually over 1 day")
    print("2. Grow automatically over 30 days")
    print("3. Report status")
    print("0. Exit program")
    print()
    print("Please select an option from the above menu")

def getMenuChoice():
    option_valid = False
    while not option_valid:
        try: 
            choice = int(input("Option selected: "))
            if 0 <= choice <= 3:
                option_valid = True
            else: 
                print("Please enter a valid option")
        except ValueError:
            print("Please enter a valid option")
    return choice

def manageCrop(crop):
    print("This is the crop management program")
    print()
    noexit = True
    while noexit:
        displayMenu()
        option = getMenuChoice()
        print()
        if option == 1:
            manualGrow(crop)
            print()
        elif option == 2:
            autoGrow(crop, 30)
            print()
        elif option == 3:
            print(crop.report())
            print()
        elif option == 0:
            noexit = False
            print()
    print("Thank you for using the program")

def main():
    newCrop = Crop(1,4,3)
    manageCrop(newCrop)

if __name__ == "__main__":
    main()