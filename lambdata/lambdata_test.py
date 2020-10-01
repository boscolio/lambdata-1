""" Basic unit tests for Lmabdata Package"""

from random import randint
import unittest
from example_module import FAVORITE_ANIMALS, increment
from oop_example import SocialMediaUser


class SocialMediaUserTest(unittest.TestCase):
  """Tests the social media class"""
  def setUp(self):
    """Common default setup code that runs before our tests"""
    self.user1 = SocialMediaUser("Jimmy", "France")
    self.user2 = SocialMediaUser("Craig", "Kenya")
    self.user3 = SocialMediaUser("Nick", "Novia Scotia", upvotes=50)

  def test_name(self):
    """ This test if the name attribute was in fact assigned properly"""
    self.assertEqual(self.user1.name, "Jimmy")
    self.assertEqual(self.user2.name, "Craig")

  def test_unpopular_popular(self):
    """ This test if the is_popular method works as intended"""
    self.assertFalse(self.user3.is_popular())
    self.user3.receive_upvotes(randint(101,1000))
    self.assertTrue(self.user3.is_popular())


class ExampleTests(unittest.TestCase):
  """Making sure examples work as expected"""
  def test_increment(self):
    """Testing increment add one to a number"""
    x0 = 0
    y0 = increment(x0)
    self.assertEqual(y0, 1)

    x1 = -1
    y1 = increment(x1)
    self.assertEqual(y1, 0)

    x2 = 10.5
    y2 = increment(x2)
    self.assertEqual(y2, 11.5)

  def test_favorite_animals(self):
    """Testing animals list"""
    self.assertIn("albino giraffe", FAVORITE_ANIMALS)
    self.assertNotIn("three tailed baby hippo", FAVORITE_ANIMALS)




if __name__ == "__main__":
  unittest.main()