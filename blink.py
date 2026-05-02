from machine import Pin
from time import sleep
 
led = Pin(22, Pin.OUT)
 
while True:
    led.toggle()
    sleep(0.5)

