class Animal:   # Parent class (superclass)
    location = "Australia"

    def __init__(self,name):
        self.name = name
    
    def speak(self):
        print("Speaking Now...")

class Dog(Animal):   # Dog inherit from Animal (Subclass of Animal )
    def speak(self):
        super().speak()
        print("Bark!!")

# a = Animal("Dog")
# a.speak()

d = Dog("Jack")
d.speak()
print(d.location)