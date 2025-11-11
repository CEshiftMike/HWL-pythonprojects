class Animal():
    def __init__(self,name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this Abstract Method")

myanimal = Animal("test")

# myanimal.speak()

class Dog(Animal):
    def speak(self):
        return self.name + "says woof"
    
class Cat(Animal):
    def speak(self):
        return self.name + "say meow !"


myanimal = Dog("joey")