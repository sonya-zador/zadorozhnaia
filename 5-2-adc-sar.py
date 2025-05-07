import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def adc():
    value = 0
    GPIO.output(dac, 0)

    GPIO.output(dac[0], 1)
    sleep(0.001)
    if(GPIO.input(comp)):
        GPIO.output(dac[0], 0)
    else:
        value += 128

    GPIO.output(dac[1], 1)
    sleep(0.001)
    if(GPIO.input(comp)):
        GPIO.output(dac[1], 0)
    else:
        value += 64

    GPIO.output(dac[2], 1)
    sleep(0.001)
    if(GPIO.input(comp)):
        GPIO.output(dac[2], 0)
    else:
        value += 32

    GPIO.output(dac[3], 1)
    sleep(0.001)
    if(GPIO.input(comp)):
        GPIO.output(dac[3], 0)
    else:
        value += 16

    GPIO.output(dac[4], 1)
    sleep(0.001)
    if(GPIO.input(comp)):
        GPIO.output(dac[4], 0)
    else:
        value += 8

    GPIO.output(dac[5], 1)
    sleep(0.001)
    if(GPIO.input(comp)):
        GPIO.output(dac[5], 0)
    else:
        value += 4

    GPIO.output(dac[6], 1)
    sleep(0.001)
    if(GPIO.input(comp)):
        GPIO.output(dac[6], 0)
    else:
        value += 2

    GPIO.output(dac[7], 1)
    sleep(0.001)
    if(GPIO.input(comp)):
        GPIO.output(dac[7], 0)
    else:
        value += 1
    
    return value

try:
    while True:
        i = adc()
        print("Цифровое значение: {:3d}, напряжение: {:.2f}".format(i, i / 256.0 * 3.3))


finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()