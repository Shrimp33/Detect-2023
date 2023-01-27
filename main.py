from gpiozero import MCP3008
from time import sleep

from aggregator import *
import logging

DELAY = 0.5
TOLERANCE = 0.02

logging.basicConfig(level=logging.DEBUG)

channel = MCP3008(channel=0, clock_pin=18, mosi_pin=24, miso_pin=23, select_pin=25)

prev = 0
res = 0
rest = time.time()
adj = 0

while True:
    # logging.debug(f"Reading from channel {channel.value}")
    # logging.debug(f"Raw Voltage: {channel.voltage}")
    raw = TODO(channel.value)
    t = time.time()
    draw = raw - prev
    dt = t - rest
    if draw != 0:
        rest = t
    slope = draw / dt
    if slope > TOLERANCE:
        adj = raw
    run(adj)
    time.sleep(DELAY)