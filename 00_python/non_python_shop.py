class Chai:

    def __init__(self, sweetness, milk_level):
        self.sweetness = sweetness
        self.milk_level = milk_level

        def sip(self):
            print("Sipping chai")

        def add_sugar(self, amount):
            print("Added the sugar")

myChai = Chai(sweetness=3, milk_level=2)

# myChai.add_sugar(3)