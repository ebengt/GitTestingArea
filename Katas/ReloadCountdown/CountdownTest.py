#!/usr/bin/python
import unittest
import Countdown

class CountdownTest(unittest.TestCase):
   def test_initial_state_of_countdown(self):
      counter = Countdown()
      self.assertTrue(counter.isStopped())

if __name__ == '__main__':
   unittest.main()
