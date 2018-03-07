#Daniel Bandler
#3/7/18
#olympics.py prints olympics logo

from ggame import *

blue = Color(0x0000FF,1)
gold = Color(0xFFD700, 1)
black = Color(0x000000, 1)
green = Color(0x008000, 1)
red = Color(0xFF0000, 1)
white = Color(0xFFFFFF, 1)
whitespace = Color(0xFFFFFF, 0)

blackOutline = LineStyle(1,black)

blueRing = CircleAsset(50, LineStyle(10, blue), whitespace)
blackRing = CircleAsset(50, LineStyle(10, black), whitespace)
redRing = CircleAsset(50, LineStyle(10, red), whitespace)
yellowRing = CircleAsset(50, LineStyle(10, gold), whitespace)
greenRing = CircleAsset(50, LineStyle(10, green), whitespace)


redRectangle = RectangleAsset(250, 50, blackOutline, red)
blueRectangle = RectangleAsset(250, 50, blackOutline, blue)
whiteRectangle = RectangleAsset(250, 50, blackOutline, white)
text = TextAsset("THE OLYMPICS ARE DOPE!!!", fill=red,style= "bold 30pt Georgia") #test, other options

Sprite(whiteRectangle, (0, 175))
Sprite(blueRectangle, (0, 225))
Sprite(redRectangle, (0, 275))
Sprite(text, (10,350))

Sprite(blueRing)
Sprite(blackRing, (120, 0))
Sprite(redRing, (240, 0))
Sprite(yellowRing, (60,50))
Sprite(greenRing, (180,50))

App().run()
