import RPi.GPIO as GPIO
from time import sleep

dac = [8, 11, 7, 1, 0, 5, 12, 6]

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]


GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)


try:
    user_input = input("Введите значение времени сигнала: ")
    try:
        while True:
            x = float(user_input)

            for i in range(256):
                GPIO.output(dac, dec2bin(i))
                sleep(x / 2 / 255)

            for i in range(254, 0, -1):
                GPIO.output(dac, dec2bin(i))
                sleep(x / 2 / 255)

    except ValueError:
        print('Введите число, а не строку')


finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print("EOP")