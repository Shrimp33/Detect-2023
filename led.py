import time
from gpiozero import LED

# Red LED pin 36
# Green LED pin 38
# Blue LED pin 40

red = LED(36)
green = LED(38)
blue = LED(40)

# Only blue works rn
blue.on()
time.sleep(5)
blue.off()