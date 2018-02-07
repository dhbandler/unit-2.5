#Daniel Bandler
#2/7/18
#graphicsDemo.py - Intro to ggame

from ggame import *

red = Color(0xFF0000,1) #this is color red, 1 is opacity
black = Color(0x000000,1) #color black
green = Color(0x00FF00,1) #color green
blue = Color(0x0000FF,1) #color blue

blackOutline = LineStyle(1,black)

redRectangle = RectangleAsset(200, 100, blackOutline, red) #(width, height, outline type, fill)
blueCircle = CircleAsset(100, blackOutline, blue) #radius, outline, fill
greenEllipse = EllipseAsset(100,50,blackOutline, green) #width, height, outline, fill
blackLine = LineAsset(50,160, blackOutline) #x endpoint (for ending), y endpoint (for ending starting from top left), linestyle
redTriangle = PolygonAsset([(0,150), (120,230), (60,450)], blackOutline, red) #endpoints (list), outline, fill

Sprite(redRectangle)
Sprite(blueCircle,(300,200)) #sprite and coordinates
Sprite(greenEllipse,(150,100))
Sprite(blackLine)
Sprite(redTriangle)

App().run()
