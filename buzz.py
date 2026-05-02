from machine import Pin, DAC
from time import sleep
import math

# IO4 active-low enables the audio amplifier
audio_enable = Pin(4, Pin.OUT)
audio_enable.value(0)

# IO26 is a DAC-capable pin
dac = DAC(Pin(26))

# Play a 440 Hz tone for 1 second
frequency = 440
duration = 1.0
sample_rate = 1000  # samples per second
num_samples = int(sample_rate * duration)

for i in range(num_samples):
    sample = int(127 + 127 * math.sin(2 * math.pi * frequency * i / sample_rate))
    dac.write(sample)
    sleep(1 / sample_rate)

# Silence and disable amplifier
dac.write(128)
audio_enable.value(1)
