import random

class Pet:
    def __init__(self, pet_name):
        self.name = pet_name
    
    def sleep(self):
        self.energy += 25
        return self
    
    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health -= 5
        self.energy -= 5
        return self


    def updateStatus(self):
        if self.energy == 0:
            self.status = 'tired'
        if self.health == 0:
            self.status = 'hungry'
        if self.health > 20:
            self.status = 'overweight'
        if self.energy > 10:
            self.status = 'energetic'
        else:
            self.status = 'content'
        return self

    def noise(self):
        print(self.sound)
        return self

class Dog(Pet):
    def __init__(self, pet_name):
        super().__init__(pet_name)
        self.type = 'dog'
        self.health = 10
        self.energy = 10
        self.sound = "woof"
        self.tricks = ['sit', 'heel', 'fetch']

class Cat(Pet):
    def __init__(self, pet_name):
        super().__init__(pet_name)
        self.type = 'cat'
        self.health = 15
        self.energy = 5
        self.sound = "meow"
        self.tricks =  ['ignore you', 'go to sleep', 'walk away']
    
class Bunny(Pet):
    def __init__(self, pet_name):
        super().__init__(pet_name)
        self.type = 'mouse'
        self.health = 1
        self.energy = 10
        self.sound = "squeek"
        self.tricks = ['binky', 'zoomy', 'boop']
