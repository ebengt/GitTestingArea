#!/usr/bin/python
import unittest
from Countdown import *

class CountdownTest(unittest.TestCase):
   def test_initial_state_of_countdown_should_be_isStopped(self):
      counter = Countdown()
      self.assertTrue(counter.isStopped())

   def test_after_starting_the_countdown_isStopped_should_be_false(self):
      counter = Countdown()
      counter.startCountDown(10)
      self.assertFalse(counter.isStopped())

   def test_after_decreaseCounter_if_counter_is_greater_than_zero_state_should_be_false(self):
      counter = Countdown()
      counter.startCountDown(10)
      counter.decreaseCounter()
      self.assertFalse(counter.isStopped())

   def test_after_decreaseCounter_if_counter_is_less_equal_than_zero_state_should_be_true(self):
      counter = Countdown()
      counter.startCountDown(1)
      counter.decreaseCounter()
      self.assertTrue(counter.isStopped())

if __name__ == '__main__':
   unittest.main()
