"""
Example tests using the standard Unittest Library
https://docs.python.org/3/library/unittest.html
"""

import unittest

# inheriting from unittest.TestCase class
class TestStringMethods(unittest.TestCase):
  
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self): 
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_in(self):
        s = "This is a nice string"
        self.assertTrue("T" in s)
        self.assertIn('T', s)

if __name__ == '__main__':
    unittest.main()