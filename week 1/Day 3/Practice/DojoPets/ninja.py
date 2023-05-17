class Ninja:
    #CONSTRUCTOR
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet



    #WALK()__METHOD
    def walk(self):
        self.pet.play()
        return self

    #FEED()__METHOD
    def feed(self):
        self.pet.eat()
        return self

    #BATH()__METHOD
    def bathe(self):
        self.pet.noise()
        return self