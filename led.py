import time
from gpiozero import LED

# Red LED gpio 16
# Green LED gpio 20
# Blue LED gpio 21

red = LED(16)
green = LED(20)
blue = LED(21)

# Blinking Test
while True:
    red.on()
    time.sleep(1)
    red.off()
    time.sleep(1)
    green.on()
    time.sleep(1)
    green.off()
    time.sleep(1)
    blue.on()
    time.sleep(1)
    blue.off()
    time.sleep(1)