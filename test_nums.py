import RPi.GPIO as GPIO

# Use broadcome board pins
GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN)     # hook
GPIO.setup(27, GPIO.IN)     # active
GPIO.setup(22, GPIO.IN)     # num

is_done = 0

while True:
    digits = ""
    while not GPIO.input(17):
        if not is_done:
           print "Hook lifted!"
        is_done = 1
        num = 0
        is_active_done = 0
        while GPIO.input(27):
            if not is_active_done:
               print "Active"
            is_active_done = 1

            if GPIO.wait_for_edge(22, GPIO.RISING, timeout=90) is not None:
                num += 0.5 # weird?
                print "pulse: " + str(num)

        if num != 0:
            numstr = "0" if (num == 10) else str(int(num))
            digits += numstr

    if digits != "":
        print digits

    if is_done:
        break

GPIO.cleanup()
