import RPi.GPIO as GPIO

DAC_PINS = [8, 11, 7, 1, 0, 5, 12, 6]  

GPIO.setmode(GPIO.BCM)
GPIO.setup(DAC_PINS, GPIO.OUT)

def to_binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

try:
    while True:

        try:
            user_input = input("Введите число от 0 до 255 (или 'q' для выхода): ").strip()
            if user_input.lower() == 'q':
                print("Завершение программы...")
                break

            num = int(user_input)
            if num < 0 or num > 255:
                print("Число должно быть от 0 до 255")
                continue
                
            GPIO.output(DAC_PINS, to_binary(num))

            volt = 3.3 * float(num) / 255
            print(f"Выходное напряжение: {volt:.2f}V")
            
        except ValueError:
            try:
                num = float(user_input)
                print("Введите целое число")
            except ValueError:
                print("Ошибка: Введено не числовое значение. Пожалуйста, введите целое число.")

finally:
    GPIO.output(DAC_PINS, 0)
    GPIO.cleanup()