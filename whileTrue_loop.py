from sense_hat import SenseHat
sense = SenseHat()

green = (125, 255, 0)
violet = (100, 0, 100)

while True:
    sense.show_message("Hello World!", 
                       text_colour = green, 
                       back_colour = violet, 
                       scroll_speed = 0.05)
