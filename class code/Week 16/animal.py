class Mammal:
    def __init__(self, species):
        self.__species = species

    def show_species(self):
        print("I am a ", self.__species)

    def make_sound(self):
        print('Grrrr')

    def get_species(self):
        return self.__species

class Dog(Mammal):
    def __init__(self):
        Mammal.__init__(self, "Dog")

    def make_sound(self):
        print("Woof woof")

    def give_treat(self):
        print('Yayyyy!')

class Cat(Mammal):
    def __init_(self):
        Mammal.__init__(self, "Cat")

    def make_sound(self):
        print("Meow meow")

mammal = Mammal('regular animal')
cat = Cat()
dog = Dog()

mammal.show_species()
cat.show_species()
dog.show_species()

mammal.make_sound()
cat.make_sound()
dog.make_sound()
#print(mammal.__species)
print(mammal.get_species())
