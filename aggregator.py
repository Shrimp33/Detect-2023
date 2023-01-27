import time
from gpiozero import LED

# Line of best fit 1.72 * 10^-3 x + 0.0553
# R^2 = 0.934

def run(n):
    red = LED(16)
    green = LED(20)
    blue = LED(21)
    RED = 1
    GREEN = 2
    BLUE = 3

    mass = 1.72 * pow(10, -3) * n + 0.0553
    print(mass + "g")

    if mass > RED:
        red.off()
        green.on()
        blue.off
    elif mass > GREEN:
        red.off()
        green.off()
        blue.on()
    else:
        red.on()
        green.on
        blue.on()
    