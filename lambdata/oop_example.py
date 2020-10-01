"""Examples of OOP"""

import numpy 
import pandas as pd 


class MyDataframe(pd.DataFrame):
  """Inhertis DF class and throws on a method"""

  def num_cells(self):  
    len(self.columns)
    return self.shape[0] * self.shape[1]
    

class BareMinimumClass:
  pass


class Complex:

  def __init__(self, realpart, imagpart):
    """
    Constructor for Complex Numbers
    Complex numbers have a real and imaginary part
    """
    # Attributes
    self.r = realpart 
    self.i = imagpart 

  # Methods
  def add(self, other_complex):
    self.r += other_complex.r
    self.i += other_complex.i

  def __repr__(self):
    return '({},{})'.format(self.r, self.i)


class SocialMediaUser:

  def __init__(self, name, location, upvotes=0):
    """Creates a User"""
    self.name = str(name)
    self.location = location
    self.upvotes = int(upvotes)

  def receive_upvotes(self, num_upvotes=1):
    self.upvotes += num_upvotes 
  
  def is_popular(self): 
    return self.upvotes > 100

class Animal:

  def __init__(self, name, weight, diet_type):
    """General Representation of Animals"""
    self.name = str(name)
    self.weight = float(weight)
    self.diet_type = diet_type

  def run(self):
    return "Vroom, Vroom, I go fast"

  def eat(self, food):
    return "Huge fan of that " + food

# Inherits from Animal class
class Sloth(Animal):

  def __init__(self, name, weight, diet_type, num_naps): 
    """Inherits from Animal Class"""
    super().__init__(name, weight, diet_type) # "super" has us grab the parents (Animal Class) attributes 
     # Attribute specifically for Sloth class
    self.num_naps = num_naps
  
  # Method specifically for Sloth class
  def say_something(self):
    return "This is a sloth of typing"

  def run(self):
    return "I am slow sloth guy"


# Will only run if we do `python oop_example.py`
if __name__ == '__main__':
  num1 = Complex(3, -5) 
  num2 = Complex(2, 6)
  num1.add(num2) 
  print(num1.r, num1.i)

  user1 = SocialMediaUser(name="Eli", location="San Francisco")
  user2 = SocialMediaUser(name="Carl", location="Costa Rica")
  user3 = SocialMediaUser(name="Carlton", location="Argentina", upvotes=60000)
  user4 =SocialMediaUser(name="George Washington", location="Djibouti", upvotes=7)
  print("Is popular: {}, num upvotes: {}".format(user2.is_popular(), user2.upvotes))

  user2.receive_upvotes(135)
  print("Is popular: {}, num upvotes: {}".format(user2.is_popular(), user2.upvotes))