import wiringpi
from time import sleep


BCM_MOTOR_CONTROL_PIN = 23

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(BCM_MOTOR_CONTROL_PIN, wiringpi.GPIO.OUTPUT)


cycles = input("Enter number of cycles to run: ")
stim_on_len = input("Enter number of seconds motor will be ON each cycle: ")
stim_off_len = input("Enter number of seconds motor will be OFF each cycle: ")



for x in range (0, cycles):


    wiringpi.digitalWrite(BCM_MOTOR_CONTROL_PIN, 1)
    sleep(stim_on_len)
    wiringpi.digitalWrite(BCM_MOTOR_CONTROL_PIN, 0)
    sleep(stim_off_len)

