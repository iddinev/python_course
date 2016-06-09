#!/usr/bin/env python3


class GameExceptions(Exception):
    pass


class _BaseUnit:

    def __init__(self, health=0, mana=0, weapon=None, cancast=False):

        if health > 0:
            self._maxhealth = health
            self._health = health
        else:
            pass  # Raise exception.

        if mana >= 0:
            self._maxmana = mana
            self._mana = mana
        else:
            pass  # Raise exception.

        self._alive = True
        self._cancast = cancast

    def is_alive(self):
        return self._alive

    def can_cast(self):
        return self._cancast

    def get_health(self):
        return self._health

    def get_mana(self):
        return self._mana

    def take_healing(self, healing_points):
        if self.is_alive() and healing_points > 0:
            if healing_points + self.get_health() >= self._maxhealth:
                self._health = self._maxhealth
            else:
                self._health += healing_points
            return True
        else:
            return False

    def take_damage(self, damage_points):
        if self.is_alive() and damage_points >= 0:
            if self.get_health() - damage_points <= 0:
                self._alive = False
            else:
                self._health -= damage_points

    def take_mana(self, mana_points):
        if self.is_alive() and mana_points > 0:
            if self.get_mana() - mana_points <= 0:
                return False
            else:
                self._mana -= mana_points
            return True
        else:
            return False

    def learn(self, spell):
        self._spell = spell
        self._cancast = True

    def equip(self, weapon):
        self._weapon = weapon

    # def attack(self, opponent=None, by=None):
    def attack(self, by=None):
        if hasattr(self, '_weapon') and by == 'weapon':
            return self._weapon.get_damage()
        elif hasattr(self, '_spell') and by == 'magic':
            return self._spell.get_damage()
        else:
            return 0


class _BaseWeapon:

    def __init__(self, name=None, damage=0):
        if damage > 0 and name is not None:
            self._damage = damage
            self._name = name
        else:
            pass  # Raise exception.

    def get_name(self):
        return self._name

    def get_damage(self):
        return self._damage


class Hero(_BaseUnit):

    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        super().__init__(health, mana)
        self._name = name
        self._title = title
        if mana_regeneration_rate > 0:
            self._mana_regeneration_rate = mana_regeneration_rate
        else:
            pass  # Raise exception.

    def known_as(self):
        return "{0} the {1}".format(self._name, self._title)


class Enemy(_BaseUnit):

    def __init__(self, health, mana, damage):
        super().__init__(health, mana)
        self._base_attack = Weapon('Base Attack', damage)

    def attack(self, by=None):
        if by is None:
            return self._base_attack.get_damage()
        else:
            return super().attack(by)


class Weapon(_BaseWeapon):
    pass


class Spell(_BaseWeapon):

    def __init__(self, name, damage, mana_cost=0, cast_range=0):
        super().__init__(name, damage)
        if mana_cost >= 0 and cast_range >= 0:
            self._mana_cost = mana_cost
            self._cast_range = cast_range
        else:
            pass  # Raise exception.

    def get_mana_cost(self):
        return self._mana_cost

    def get_cast_range(self):
        return self._cast_range
