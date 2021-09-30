# import the class that you want to inherit
from Chef import Chef

# put inherit class into new class
class ChineseChef(Chef):

    def makeSpecialDish(self):
        print("The chef makes orange chicken")

    def makeFriedRice(self):
        print("The chef makes fried rice")