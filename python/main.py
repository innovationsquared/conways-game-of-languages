import pygame as py
import numpy as np
from const import *
from city import City
#from cell import Cell 
class Main:
   def __init__(self):
      py.init()
      self.SCREEN= py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
      py.display.set_caption("Game of Life")
      self.clock = py.time.Clock()
      self.city = City()
      #self.cell = Cell()


   def mainLoop(self):
      running = True
      screen = self.SCREEN
      clock = self.clock
      city = self.city
      arr = city.initializeCity()
      

      while running:
         screen.fill('grey')
         for event in py.event.get():
            if event.type == py.QUIT:
               running = False
         arr = city.evolve(arr)
         city.drawScreen(screen, arr)
         py.display.flip()
         clock.tick(20)
      py.quit() 

main = Main()
main.mainLoop()