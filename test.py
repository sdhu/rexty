import RPi.GPIO as GPIO
import gpios

# Use broadcom board pins
GPIO.setmode(GPIO.BCM)

GPIO.setup(gpios.HOOK, GPIO.IN)
GPIO.setup(gpios.IDLE, GPIO.IN)
GPIO.setup(gpios.NUM, GPIO.IN)

is_done = 0

while True:
    digits = ""
    while not GPIO.input(gpios.HOOK):
        if not is_done:
           print "Hook lifted!"
        is_done = 1
        num = 0
        is_active_done = 0
        while GPIO.input(gpios.IDLE):
            if not is_active_done:
               print "Active"
            is_active_done = 1

            if GPIO.wait_for_edge(gpios.NUM, GPIO.FALLING, timeout=90) is not None:
                num += 1 # weird with RISING and BOTH?
                print "pulse: " + str(num)

        if num != 0:
            numstr = "0" if (num == 10) else str(num)
            digits += numstr

    if digits != "":
        print digits

    if is_done:
        break

GPIO.cleanup()
