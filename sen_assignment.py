class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("Munch munch!")

    def sleep(self):
        print("Zzzzzzzz!")


class Dog(Animal):

    def __init__(self, name, age, breed):
        self.breed = breed

        Animal.__init__(self, name, age)

    def bark(self):
        print("Woof!")


class Horse(Animal):

    def __init__(self, name, age, breed, hoof_print):
        self.breed = breed
        self.hoof_print = hoof_print

        Animal.__init__(self, name, age)

    def neigh(self):
        print("Neigh!")

    def gallop(self):
        print("Galloping...")


dog1 = Dog("Bruno", 10, "German Shepherd")
print("Name:", dog1.name)
print("Age:", dog1.age)
print("Breed:", dog1.breed)
dog1.eat()
dog1.sleep()
dog1.bark()

print("")

horse1 = Horse("River", 15, "Mustang", "Stubby")
print("Name:", horse1.name)
print("Age:", horse1.age)
print("Breed:", horse1.breed)
horse1.eat()
horse1.sleep()
horse1.neigh()
horse1.gallop()
