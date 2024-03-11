import turtle
import random

colors = [(1, 9, 30), (121, 95, 41), (72, 32, 21), (238, 212, 72), (220, 81, 59), (226, 117, 100), (93, 1, 21),
          (178, 140, 170), (151, 92, 115), (35, 90, 26), (6, 154, 73), (205, 63, 91), (168, 129, 78), (3, 78, 28),
          (1, 64, 147), (221, 179, 218), (4, 220, 218), (80, 135, 179), (130, 157, 177), (81, 110, 135),
          (120, 187, 164),
          (11, 213, 220), (118, 18, 36), (243, 205, 7), (132, 223, 209), (229, 173, 165), (70, 70, 45), (185, 190, 201),
          (126, 225, 231), (88, 49, 45), (61, 65, 66)]


def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])


# Convert RGB tuples to hexadecimal color strings
hex_colors = [rgb_to_hex(color) for color in colors]

tim = turtle.Turtle()
tim.speed("fastest")
tim.penup()

for i in range(10):
    ini_x = -400
    ini_y = -300 + i * 70
    for j in range(10):
        tim.color(random.choice(hex_colors))
        tim.goto(ini_x, ini_y)
        tim.dot(30)

        ini_x += 90

    ini_y += 100

screen = turtle.Screen()
screen.exitonclick()
