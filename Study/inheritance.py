class Animal():
    def __init__(self):
        print("Animal created")
    # def who_am_i(self):
    #     print("im an animal")
    # def i_am_eating(self):
    #     print("animal is eating")
    def sound(Self):
        print("there is no sound, define animal first")

# myanime = Animal()

# myanime.i_am_eating()

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog is created")


# myanime = Dog()

Dog().i_am_eating()