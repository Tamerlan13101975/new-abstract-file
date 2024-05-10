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


class Hammer(Weapon):
    def attack(self):
        print("Наносит удары")


class Fighter():
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def changeWeapon(self, weapon: Weapon):
            self.weapon = weapon

    def fight(self):
        print(self.weapon.attack())


class Monster():
    def __init__(self, weapon: Weapon):
        self.weapon = weapon


hammer = Hammer()

sword = Sword()

bow1 = Bow()


fighter = Fighter(Sword())

fighter.fight()


fighter.changeWeapon(bow1)


fighter.fight()













