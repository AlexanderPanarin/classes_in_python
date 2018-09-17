class Animal:
    def __init__(self, tail, paw, wool,):
        self.tail = tail
        self.paw = paw
        self.wool = wool
some_animal = Animal
some_animal.tail = 1
some_animal.paw = 4
some_animal.wool = True

class Dog(Animal):
    def __init__(self, tail, paw, wool, say_something ):
        self.tail = tail
        self.paw = paw
        self.wool = wool
        self.say_something = say_something
doggy = Dog
doggy.tail = 1
doggy.paw = 4
doggy.wool = True
doggy.say_something = "Woof-woof"

class Cat(Animal):
    def __init__(self, tail, paw, wool, say_something):
        self.tail = tail
        self.paw = paw
        self.wool = wool
        self.say_something = say_something
kitty = Cat
kitty.tail = 1
kitty.paw = 4
kitty.wool = True
kitty.say_something = "Meow-meow"

class SphynxCat(Cat):
    def __init__(self, tail, paw, wool, say_something):
        self.tail = tail
        self.paw = paw
        self.wool = wool
        self.say_something = say_something
sphynx = SphynxCat
sphynx.tail = 1
sphynx.paw = 4
sphynx.wool = False
sphynx.say_something = "murr-murr"

class Rooster(Animal):
    def __init__(self, tail, paw, wool, say_something):
        self.tail = tail
        self.paw = paw
        self.wool = wool
        self.say_something = say_something
petya = Rooster
petya.tail = 1
petya.paw = 2
petya.wool = False
petya.say_something = "Cocorico"
