#!/usr/bin/env python3


import decorators
import unittest


class TestDecorators(unittest.TestCase):

    def test_accepts(self):
        self.assertEqual(decorators.test_accepts('asd', 5), 'asd, 5')
        self.assertRaises(ValueError, decorators.test_accepts, 'asd')
        self.assertRaises(TypeError, decorators.test_accepts, 'asd', '5')

    def test_encrypt(self):
        self.assertEqual(decorators.test_encrypt(), 'b c d e')


if __name__ == "__main__":
    unittest.main()
