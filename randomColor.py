from sense_hat import SenseHat
from random import randint

sense = SenseHat()

# RGB Color Values
r = randint(0,255)
g = randint(0,255)
b = randint(0,255)

sense.clear((r, g, b))
