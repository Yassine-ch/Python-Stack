import ninja
import pets


#INSTACE_OF_PET
pet_1 = pets.Pet("kiba", "dog", ["sit", "down", "shake", "stand"])
#INSTANCE_OF_NINJA
ninja_1 = ninja.Ninja("Diego", "Carrera", "Freeze Dried Beef", "Kibble", pet_1)

#CALL_METHOD_IN_NINJA
ninja_1.feed().walk().bathe()

#PET_INFO
print(pet_1.health, pet_1.energy,pet_1.name)

#INSTANCE_OF_DOG_(A CHILD_CLASS_OF_PET)
dog_1 = pets.Dog("Juneau", "dog", ["sit"], "Alaskian Malamute", False)