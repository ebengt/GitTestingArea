#!/usr/bin/python
import unittest
from Countdown import *

class CountdownTest(unittest.TestCase):
   def test_initial_state_of_countdown_should_be_isStopped(self):
      counter = Countdown()
      self.assertTrue(counter.isStopped())

   def test_after_starting_the_countdown_isStopped_is_false(self):
      counter = Countdown()
      counter.startCountDown(10)
      self.assertFalse(counter.isStopped())

if __name__ == '__main__':
   unittest.main()
