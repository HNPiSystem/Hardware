import RPi.GPIO as GPIO
import time, os
import subprocess

pir_sensor_flag = -1
camera_flag = -1
thermo_sensor_flag = -1
light_sensor_flag = -1

GPIO.cleanup()

def check_pir_sensor():
	
	global pir_sensor_flag
	print "PIR module check test!"

	GPIO.setmode(GPIO.BCM)

	GPIO_PIR = 7
	GPIO_LED = 23

	GPIO.setup(GPIO_PIR, GPIO.IN)
	GPIO.setup(GPIO_LED, GPIO.OUT)
	
	Current_State = 0

	try:
		while GPIO.input(GPIO_PIR)==1:
			Current_State = 0

		Current_State = GPIO.input(GPIO_PIR)

		if Current_State == 1:
			print "PIR module is connected!"
			pir_sensor_flag = 1
		else:
			print "PIR module is not connected!"


		GPIO.cleanup()
                print "----------------------------"		
		return pir_sensor_flag

	except:
		print("error!")
		GPIO.cleanup()
		return 0
		
	
def check_camera():
	global camera_flag
	print "CAMERA module check test!"

	test = "raspistill -v"
	t1 = os.system(test)
	
	try:
                if t1 == 0:
                        print "camera_module is connected"
                        camera_flag = 1
                else:
                        print "camera_module is not connected"

                print "----------------------------"
                return camera_flag

        except:
                print("error!")
		return 0

def check_thermo_sensor():
	global thermo_sensor_flag
	print "THERMOMETER module check test!"

	test1 = "sudo modprobe w1-gpio"
	test2 = "sudo modprobe w1-therm"
	test3 = "cat /sys/bus/w1/devices/10-00080230a78c/w1_slave | grep -E -o \".{0,0}t=.{0,5}\" | cut -c 3-"

	t1 = os.system(test1)
	t2 = os.system(test2)


	pipe = subprocess.Popen(test3, shell=True, stdout=subprocess.PIPE)
	pipe.wait()

	result = pipe.stdout.read()
	result = result[0 : len(result)-2]

        try:
                if not result == "":
                        print "thermo_sensor is connected"
                        thermo_sensor_flag = 1
                else:
                        print "thermo_sensor is not connected"

                print "----------------------------"
                return thermo_sensor_flag


        except:
                print("error!")
                return 0



def check_light_sensor():

	global light_sensor_flag
	print "LIGHTSENSOR module check test!"

	GPIO.setmode(GPIO.BCM)
	GPIO.setup(18, GPIO.OUT)
	GPIO.output(18, GPIO.LOW)
	GPIO.setup(18, GPIO.IN)
	
	try:
		for i in range(0, 100, 1):
			if (GPIO.input(18) == 1):
				print "Light_sensor is connected"
				light_sensor_flag = 1
				break
			elif light_sensor_flag == 1:
				break
			else:
				print "Light_sensor module is not connected"
	                
		print "----------------------------"
		GPIO.cleanup()
		return light_sensor_flag

	except:
		print("error!")
		GPIO.cleanup()
		return 0
