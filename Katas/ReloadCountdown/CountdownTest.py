#!/usr/bin/python
import unittest
from Countdown import *

class CountdownTest(unittest.TestCase):
   def test_initial_state_of_countdown(self):
      counter = Countdown()
      self.assertTrue(counter.isStopped())

if __name__ == '__main__':
   unittest.main()
