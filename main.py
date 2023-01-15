from gpiozero import MCP3008
from time import sleep

from aggregator import *
import logging

DELAY = 0.5

logging.basicConfig(level=logging.DEBUG)

channel = MCP3008(channel=0, clock_pin=18, mosi_pin=24, miso_pin=23, select_pin=25)

while True:
    logging.debug(f"Reading from channel {channel.value}")
    logging.debug(f"Raw Voltage: {channel.voltage}")
    res = TODO(channel.value)
    sleep(DELAY)