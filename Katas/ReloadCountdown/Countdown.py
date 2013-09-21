#!/usr/bin/python

class Countdown:
   def __init__(self):
      self.counter = 0;

   def isStopped(self):
      # The Countdown state is isStopped if self.counter 
      # is less or equal than zero.
      return (self.counter <= 0);

   def startCountDown(self, seconds):
      # Initialize the counter.
      self.counter = seconds;

   def decreaseCounter(self):
      self.counter = self.counter - 1;
