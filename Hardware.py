import camera
import pir_sensor
import module_check
import subprocess
import os

class HardwareManager():

	# connected module check flag
	# flag -> -1 : not connected / 1 : connected
	picamera = -1
	thermo_sensor = -1
	light_sensor = -1	


	# initialize
	def __init__(self):

		# connected module check
		#self.picamera = module_check.check_camera()
		#self.thermo_sensor = module_check.check_thermo_sensor()
		self.light_sensor = module_check.check_light_sensor()


	# return connected module info ##
	def status_of_cctv(self):
		return self.picamera
	def status_of_therm(self):
		return self.thermo_sensor
	def status_of_light(self):
		return self.light_sensor
	#################################


	# send all connected modules info ####
	def get_status_of_devices(self):
		devices = []
		if self.status_of_cctv() == 1:
			devices.append('cctv_module')
		if self.status_of_therm() == 1:
			devices.append('therm_module')
		if self.status_of_light() == 1:
			devices.append('light_module')
		return devices


	# ask for camera module,
	# execute camera module after status check
	def ask_camera(self):
		try:
			# for testing ##################
			print("in ask_camera")
			################################

			# take picture and image's path return to Server
			self.image_path = camera.camera_execute()
			print(self.image_path)
			return self.image_path

		except:
			print("error - ask_camera!")
			return -1

		# for testing #################
                print("out ask_pir_sensor")
                ###############################



	# ask for streaming module,
	# execute streaming module after status check
	def ask_streaming(self):
		try:
			# for testing ##################
			print("in ask_streaming")
			#################################

			# execute streaming service
			camera.view_stream()
			print("quit to streaming")

		except:
			print("error - ask_streaming!")
			return -1

		# for testing #################
                print("out ask_pir_sensor")
                ###############################


		
	# ask for pir_sensor module,
	# execute pir_sensor module after status check
	def ask_pir_sensor(self):
		try:
			# for testing ###################
			print("in ask_pir_sensor")
			#################################

			# execute pir_sensor
			pir_sensor.sensoring()
			print("quit to pir_sensoring")

		except:
			print("error - in ask_pir_sensor!")
			return -1
		
		# for testing #################
                print("out ask_pir_sensor")
                ###############################



        # ask for thermo_sensor module,
        # execute thermo_sensor module after status check
        def ask_thermo_sensor(self):

		text1 = "sudo modprobe w1-gpio"
		text2 = "sudo modprobe w1-therm"
		text3 = "cat /sys/bus/w1/devices/10-00080230a78c/w1_slave | grep -E -o \".$-o \".{0,0}t=.{0,5}\" | cut -c 3-"

		try:
			# for testing ###################
			print("in ask_thermo_sensor")
                	#################################

		        # execute thermo_sensor
			t1 = os.system(text1)
			t2 = os.system(text2)

			pipe = subprocess.Popen(text3, shell=True, stdout=subprocess.PIPE)
			pipe.wait()

			result = pipe.stdout.read()
			result = result[0 : len(result)-2]

			print "1"
			print result
			print "2"

			return result

		except:
			print("error - in ask_thermo_sensor!")
			return 0
		
		# for testing #################
                print("out ask_thermo_sensor")
                ###############################
