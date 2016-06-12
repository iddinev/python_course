#!/usr/bin/env python3

from dungeons_and_pythons import *
import unittest


class TestHero(unittest.TestCase):

    def testknown_as(self):
        testobj = Hero(name="Bron", title="Dragonslayer", health=100, mana=200,
                       mana_regeneration_rate=2)
        self.assertEqual("Bron the Dragonslayer", testobj.known_as())

    def testattack(self):
        testobj = Enemy(health=100, mana=20, damage=10)
        testobj.equip(Weapon('testobj sword', damage=20))
        self.assertEqual(10, testobj.attack())
        self.assertEqual(20, testobj.attack('weapon'))


if __name__ == "__main__":
    Map = Dungeon('level.txt')
    Map.print_map()
    print(Map.get_starting_points())
    unittest.main()
