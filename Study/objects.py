class MyFirstClass():
    property1 = "Michael"
    def __init__(self, name):
        self.name = self.property1
        # print("hello world!")
        # return "Hello World!"
    
    def saysomething(self):
        return "I want to say hello"

class SecondClass(MyFirstClass):
    def __init__(self, name):
        MyFirstClass.__init__(self, name)
        print(f"Inheritance is a Success! - Parameter: name = {name}")
    
    def saysomething(self):
        return "I want to say Hi !"
    
class FirstAbstract():
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("You are suppose to inherit this class")
    


alpha1 = MyFirstClass("mike")

alpha2 = SecondClass("totoy")

alpha3 = FirstAbstract("JuMong")

# print(alpha1)