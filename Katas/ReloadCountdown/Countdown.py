#!/usr/bin/python

class Countdown:
   def __init__(self):
      self.started = False;

   def isStopped(self):
      return not self.started;

   def startCountDown(self, seconds):
      self.started = True;
