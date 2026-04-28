class Animal:
    def __init__(self, name):
        self.name = name 

    def speak(self):
        return "animal sound"
    
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"  
    
class Cat(Animal):
    def speak (self):
        return f"{self.name} says Meaow!"
       
my_dog = Dog("Buddy")
my_cat = Cat("Whiskers")

print(my_dog.speak()) # Output: Buddy says Woof!
print(my_cat.speak()) #Output: Whiskers says Meaow!
