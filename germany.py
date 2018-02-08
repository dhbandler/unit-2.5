#Daniel Bandler
#2/8/18
#germany.py displays the german flag

from ggame import *

black = Color(0x000000, 1)
red = Color(0xff0000, 1)
yellow = Color(0xffff00, 1)
white = Color(0xffffff, 1)


blackOutline = LineStyle(1,black)

blackRectangle = RectangleAsset(250, 50, blackOutline, black)
redRectangle = RectangleAsset(250, 50, blackOutline, red)
yellowRectangle = RectangleAsset(250, 50, blackOutline, yellow)
whiteRectangle = RectangleAsset(250, 50, blackOutline, white)

Sprite(blackRectangle)
Sprite(redRectangle, (0, 50))
Sprite(yellowRectangle, (0, 100))

Sprite(blackRectangle, (400, 0))
Sprite(whiteRectangle, (400, 50))
Sprite(redRectangle, (400, 100))





App().run()
