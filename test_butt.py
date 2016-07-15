import RPi.GPIO as GPIO
import gpios
from statemachine import StateMachine

# Use broadcom board pins
GPIO.setmode(GPIO.BCM)

# Active low signals
GPIO.setup(gpios.CLEAR, GPIO.IN)
GPIO.setup(gpios.BUTT1, GPIO.IN)
GPIO.setup(gpios.BUTT2, GPIO.IN)
GPIO.setup(gpios.BUTT3, GPIO.IN)
GPIO.setup(gpios.BUTT4, GPIO.IN)
GPIO.setup(gpios.BUTT5, GPIO.IN)

butt_num = 0

def idle_state(val):
    print "IDLE: "
    while 1:
        if not GPIO.input(gpios.BUTT1):
            newState = "BUTT"; butt_num = 1; break;
        elif not GPIO.input(gpios.BUTT2):
            newState = "BUTT"; butt_num = 2; break;
        elif not GPIO.input(gpios.BUTT3):
            newState = "BUTT"; butt_num = 3; break;
        elif not GPIO.input(gpios.BUTT4):
            newState = "BUTT"; butt_num = 4; break;
        elif not GPIO.input(gpios.BUTT5):
            newState = "BUTT"; butt_num = 5; break
    print str(butt_num) + " >> "
    return (newState, val)

def butt_state(val):
    print "BUTT: "
    while 1:
        if not GPIO.input(gpios.BUTT1):
            butt_num = 1; print str(butt_num);
        elif not GPIO.input(gpios.BUTT2):
            butt_num = 2; print str(butt_num);
        elif not GPIO.input(gpios.BUTT3):
            butt_num = 3; print str(butt_num);
        elif not GPIO.input(gpios.BUTT4):
            butt_num = 4; print str(butt_num);
        elif not GPIO.input(gpios.BUTT5):
            butt_num = 5; print str(butt_num);
        else:
            butt_num = 0; break
    print " >> "
    return (newState, val)

def end_state(val):
    print "END: "
    return ("END", 0)

if __name__== "__main__":
    m = StateMachine()
    m.add_state("IDLE", idle_state)
    m.add_state("BUTT", butt_state)
    m.add_state("END", end_state, end_state=1)
    m.set_start("IDLE")
    m.run(1)

GPIO.cleanup()
