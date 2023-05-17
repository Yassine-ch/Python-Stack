class Pet:
    #! CONSTRACTOR
    def __init__(self,name,pet_type,tricks):
        self.name=name
        self.type = pet_type
        self.tricks = tricks
        self.health = 40
        self.energy = 40
    #METHODS
        # SLEEP()_METHOD_INCREASE_THE_PET_ENERGY_BY_25
    def sleep(self):
        self.energy += 25
        return self
    #EAT()_METHOD_INCREASE_THE_PET_ENERGY_BY_&&&_HEALTH_BY_10

    def eat(self):
        self.energy += 5
        self.health += 10
        return self
    #PLAY()_METHOD_INCREASE_THE_PET_HEALTH_BY_5
    def play(self):
        self.health += 5
        return self

    #NOISE()_PRINT_OUT_THE_PET_SOUND
    def noise(self):
        print("WOOOOF")
        return self
#!!!!! CLASS DOG____FROM PET
class Dog(Pet):
    def __init__(self, name, pet_type, tricks, is_hypoallergenic):
        super().__init__(name, pet_type, tricks)
        self.is_hypoallergenic = is_hypoallergenic