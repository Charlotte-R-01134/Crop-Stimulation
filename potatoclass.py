from cropclass import *

class Potato(Crop):
    """ A potato crop"""

    def __init__(self):
        super().__init__(1,3,6)
        self.type = "Potato"
    
    def grow(self, light, water):
        if light >= self.lightNeed and water >= self.waterNeed:
            if self.status == "Seedling" and water > self.waterNeed:
                self.growth += self.growthRate * 1.5
            elif self.status == "Young" and water > self.waterNeed:
                self.growth += self.growthRate * 1.25
            else:
                self.growth += self.growthRate
        self.daysGrowing += 1
        self.updateStatus()

def main():
    potatoCrop = Potato()
    print(potatoCrop.report())
    manualGrow(potatoCrop)
    print(potatoCrop.report())
    manualGrow(potatoCrop)
    print(potatoCrop.report())

if __name__ == "__main__":
    main()
