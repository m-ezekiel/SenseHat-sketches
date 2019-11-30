from sense_hat import SenseHat
sense = SenseHat()

# Change rotation
sense.set_rotation(180)

# Define Colors
r = (255, 0 , 0)
g = (0, 255 , 0)
b = (0, 0, 255)

y = (255, 255, 0)
v = (255, 0, 255)
a = (0, 255, 255)

w = (255, 255, 255)
k = (0, 0, 0)

pixel_map = [
    w,k,k,k,k,k,k,k,
    w,w,k,k,k,k,k,k,
    w,w,w,k,k,k,k,k,
    w,w,w,w,k,k,k,k,
    w,w,w,w,w,k,k,k,
    w,w,w,w,w,w,k,k,
    w,w,w,w,w,w,w,k,
    w,w,w,w,w,w,w,w
]

sense.set_pixels(pixel_map)