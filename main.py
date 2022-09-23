import keyboard
import neopixel
import board

num_lights = 50

# program 50 lights with the default brightness 1.0, and autoWrite true
pixels = neopixel.NeoPixel(board.D18, num_lights)

pixel = 0

while True:
    if keyboard.read_key() == "right":
        pixel += 1
        print(pixel)
    if keyboard.read_key() == "left":
        pixel -= 1
        print(pixel)
    if keyboard.read_key() == "x":
        # turn off neopixels
        pixels.fill((0, 0, 0))

    # light up a given pixel in red
    if keyboard.read_key() == "r":
        pixels[pixel]((255, 0, 0))

    # light up a given pixel in green
    if keyboard.read_key() == "g":
        pixels[pixel]((0, 255, 0))

    # light up a given pixel in red
    if keyboard.read_key() == "b":
        pixels[pixel]((0, 0, 255))
