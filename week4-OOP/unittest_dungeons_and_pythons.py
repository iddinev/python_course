#!/usr/bin/env python3

from dungeons_and_pythons import Hero
import unittest


class TestHero(unittest.TestCase):


    def testknown_as(self):
        testobj = Hero(name="Bron", title="Dragonslayer", health=100, mana=100,
                       mana_regeneration_rate=2)
        self.assertEqual("Bron the Dragonslayer", testobj.known_as())

    def test

if __name__ == "__main__":
    unittest.main()
