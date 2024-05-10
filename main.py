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





