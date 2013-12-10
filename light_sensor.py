import RPi.GPIO as GPIO, time, os      
import time

#DEBUG = 1
#GPIO.setmode(GPIO.BCM)

#power_pin = 23

#GPIO.setup(power_pin, GPIO.OUT)
#GPIO.output(power_pin, False)

def RCtime (RCpin):
        reading = 0
        GPIO.setup(RCpin, GPIO.OUT)
        GPIO.output(RCpin, GPIO.LOW)
        time.sleep(1)

        GPIO.setup(RCpin, GPIO.IN)
        while (GPIO.input(RCpin) == GPIO.LOW):
                reading += 1
        return reading

def light_sensoring():
	GPIO.cleanup()
	GPIO.setmode(GPIO.BCM)
	
	power_pin = 23

	GPIO.setup(power_pin, GPIO.OUT)
	GPIO.output(power_pin, False)

	try:
		while True:
			test = RCtime(18)
			if test > 3500:
				print test
				print("POWER ON")
				GPIO.output(power_pin, True)
			elif test <= 3500:
				print test
				print("POWER OFF")
				GPIO.output(power_pin, False)

	except:
		GPIO.cleanup()
		print("error!")	


def light_relay_on():
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)

        power_pin = 23

        GPIO.setup(power_pin, GPIO.OUT)
        GPIO.output(power_pin, False)

	try:
		GPIO.output(power_pin, True)
		return "True"
	except:
		GPIO.cleanup()
		print("error!")
		return "False"


def light_relay_off():
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)

        power_pin = 23

        GPIO.setup(power_pin, GPIO.OUT)
        GPIO.output(power_pin, False)

	try:
		GPIO.output(power_pin, False)
		return "True"
	except:
		GPIO.cleanup()
		print("error!")
		return "False"
