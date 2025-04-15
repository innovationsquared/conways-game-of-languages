import pygame as py
import numpy as np
from const import *
class Main:
   def __init__(self):
      py.init()
      self.SCREEN= py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
      py.display.set_caption("Game of Life")
      self.clock = py.time.Clock()

   def mainLoop(self):
      running = True
      screen = self.SCREEN
      clock = self.clock
      while running:
         screen.fill('grey')
         for event in py.event.get():
            if event.type == py.QUIT:
               running = False
         py.display.flip()
         clock.tick(60)
      py.quit() 

main = Main()
main.mainLoop()