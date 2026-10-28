class Dog:
    def __init__(self, name ,breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woef")

dog_1 = Dog(name="Sepp",breed="Rich-Back")
print(dog_1.name)
dog_1.bark()