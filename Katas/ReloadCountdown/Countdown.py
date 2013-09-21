#!/usr/bin/python

class Countdown:
   def __init__(self):
      self.started = False;
      self.counter = 0;

   def isStopped(self):
      return not self.started;

   def startCountDown(self, seconds):
      self.started = True;

   def decreaseCounter(self):
      self.counter = self.counter - 1;
