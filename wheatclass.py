from cropclass import *

class Wheat(Crop):
    """A wheat crop"""

    def __init__(self):
        super().__init__(1,2,4)
        self.type = "Wheat"
    
    def grow(self, light, water):
        if light >= self.lightNeed and water >= self.waterNeed:
            if self.status == "Seedling": 
                self.growth += self.growthRate * 1.5
            elif self.status == "Young":
                self.growth += self.growthRate * 1.25
            elif self.status == "Old":
                self.growth += self.growthRate / 2
            else:
                self.growth += self.growthRate
        self.daysGrowing += 1
        self.update_status()

def main():
    wheatCrop = Wheat()
    print(wheatCrop.report())
    manualGrow(wheatCrop)
    print(wheatCrop.report())
    manualGrow(wheatCrop)
    print(wheatCrop.report())

if __name__ == "__main__":
    main()