import DojoPets as dp
import random

class Ninja:
    def __init__(self, first_name, last_name, pet_name, pet_type):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = 3
        self.pet_food = 3
        if pet_type == 'dog':
            self.pet = dp.Dog(pet_name)
        if pet_type == 'cat':
            self.pet = dp.Cat(pet_name)
        if pet_type == 'bunny':
            self.pet = dp.Bunny(pet_name)
    
    def walk(self):
        if self.pet.health <= 0:
            print(f"{self.pet.name} doesn't want to go on a walk, they look hungry")
        if self.treat <= 0:
            print(f"{self.pet.name} doesn't want to go on a walk, you don't have any treats")
        else:
            self.pet.play()
            self.treats -= 1
            print(f"Walking {self.pet.name}, and they look {self.pet.status}")
            return self

    def feed(self):
        if self.pet_food > 0: 
            print(f"Feeding {self.pet.name}, and they look {self.pet.status}")    
            self.pet.eat()
            self.pet_food -= 1
        else:
            print("Oh no! Your out of food!")
        return self

    def bathe(self):
        self.pet.noise()
        return self

    def do_a_trick(self):
        if self.treats <= 0:
            print(f"{self.pet.name} doesn't want to do a trick, you don't have any treats")
        if self.pet.energy <= 0:
            print(f"{self.pet.name} doesn't want to do a trick, they are too tired")
        else:
            trick = random.choice(self.pet.tricks)
            print(f"{self.pet.name} decides to {trick}")
            self.treats -=1

        return self

    def put_to_bed(self):
        self.pet.sleep()
        return self

    def get_more_food(self, amount):
        self.pet_food += amount
        return self

    def get_more_treats(self, amount):
        self.treats += amount
        return self


ninja1 = Ninja("Bruce", "Wayne", "Bowser", 'cat')

ninja1.do_a_trick().do_a_trick().do_a_trick().do_a_trick().do_a_trick().get_more_treats(15).do_a_trick().do_a_trick().do_a_trick().do_a_trick().do_a_trick().do_a_trick()
