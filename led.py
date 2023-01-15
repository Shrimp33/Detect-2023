import time
from gpiozero import LED

# Red LED gpio 16
# Green LED gpio 20
# Blue LED gpio 21

red = LED(16)
green = LED(20)
blue = LED(21)

# Only blue works rn
blue.on()
time.sleep(10.0)
blue.off()