import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)

p = GPIO.PWM(24, 1000)
p.start(0)

try:
    while True:
        user_input = int(input())
        p.ChangeDutyCycle(user_input)
        print(3.3 * user_input / 100)

finally:
    p.stop()
    GPIO.output(24,0)
    GPIO.cleanup()