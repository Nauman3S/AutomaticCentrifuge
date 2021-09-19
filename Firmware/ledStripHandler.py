import board
import neopixel
import time
pixels = neopixel.NeoPixel(board.D21, 60,brightness=1, pixel_order=neopixel.RGBW)

def ledState(v):
    global pixels
    if(v=='red'):
        pixels.fill((255, 0, 0))
    if(v=='white'):
        pixels.fill((255, 255, 255))

    elif(v=='green'):
        pixels.fill((0, 255, 0))
    elif(v=='blue'):
        pixels.fill((0, 0, 255))
    elif(v=='off'):
        pixels.fill((0, 0, 0))
    pixels.show()


