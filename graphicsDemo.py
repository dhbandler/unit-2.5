#Daniel Bandler
#2/7/18
#graphicsDemo.py - Intro to ggame

from ggame import *

red = Color(0xFF0000,1) #this is color red
black = Color(0x000000,1) #this is the color black

blackOutline = LineStyle(1,black)

redRectangle = RectangleAsset(200, 100, blackOutline, red) #(width, height, outline type, fill)

Sprite(redRectangle)


App().run()
