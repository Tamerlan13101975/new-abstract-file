from abc import ABC, abstractmethod


class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


class Sword(Weapon):
    def attack(self):
        print("Боец наносит удары мечом")

class Bow(Weapon):
    def attack(self):
        print("Боец совершает выстрелы из лука")



class Fighter():
    def __init__(self, weapon: Weapon):
        self. weapon = weapon

    def changeWeapon(self, weapon: Weapon):
            self.weapon = weapon

    def fight(self):
        print(self.weapon.attack())














