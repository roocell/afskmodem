from afskmodem import DigitalTransmitter
from afskmodem import DigitalModes
import time
transmitter = DigitalTransmitter(DigitalModes.afsk300())
print("AFSKmodem TX Demo")

# does better with padding
message = """
------
This should be a breeze.
But it doesn’t come for free.
Something that freshens the air.
But, on the inside, it’s contents are nowhere.
------"""

while True:
    transmitter.tx(message.encode("ascii", "ignore"))
    time.sleep(5)
