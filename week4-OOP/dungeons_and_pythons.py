#!/usr/bin/env python3

class GameExceptions(Exception):


class BaseUnit:

    def __init__(self, name=None, title=None, health=0, mana=0,
                 mana_regeneration_rate=0, weapon=None):

        if health > 0:
            self._maxhealth = health
            self._health = health
        else:
            pass # Raise exception.

        if mana > 0:
            self._maxmana = mana
            self._mana = mana
        else:
            pass # Raise exception.

        self._alive = True
        self._mana_regeneration_rate = mana_regeneration_rate



    def is_alive(self):
        pass

    def can_cast(self):
        pass

    def get_health(self):
        pass

    def get_mana(self):
        pass

    def take_healing(self):
        pass

    def take_damage(self):
        pass

    def take_mana(self):
        pass

    def learn(self):
        pass

    def equip(self):
        pass

    def attack(self):
        pass


class BaseWeapon:
    pass


class Hero(BaseUnit):

    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        self.name = 'wtf'

    def known_as(self):
        return "blah"

class Enemy(BaseUnit):
    pass

class Spell(BaseWeapon):
    pass

class Weapon(BaseWeapon):
    pass
