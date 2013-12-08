import camera
import pir_sensor
import send_email
from multiprocessing import Process, Pipe
import module_check

class HardwareManager():


	camera_execute_flag = -1
	pir_execute_flag = -1

	
	# connected module check flag
	# flag -> -1 : not connected / 1 : connected
	picamera = -1
	thermo_sensor = -1
	light_sensor = -1	


	# initialize
	def __init__(self):

		# connected module check
		self.picamera = module_check.check_camera()
		self.thermo_sensor = module_check.check_thermo_sensor()
		self.light_sensor = module_check.check_light_sensor()


	# send connected module info to Server ###
	def send_to_server_camera(self):
		return self.picamera
	def send_to_server_thermo(self):
		return self.thermo_sensor
	def send_to_server_light(self):
		return self.light_sensor
	##########################################



	# ask for camera module,
	# execute camera module after status check
	def ask_camera(self):

		# for testing ##################
		print("in ask_camera")
		print("camera flag")
		print(self.camera_execute_flag)
		################################

		# if camera module is not used
		# take picture and image's path return to Server
		if self.camera_execute_flag == -1:
			self.camera_execute_flag = 1
			self.image_path = camera.camera_execute()
			self.camera_execute_flag = -1
			print(self.image_path)
			return self.image_path
	
		# if camera module is used
		# send error message to Server and return error code -1
		else:
			print("sorry, camera module is used")
			return -1

		# for testing ################
		print("out ask_camera")
		##############################



	# ask for streaming module,
	# execute streaming module after status check
	def ask_streaming(self):

		# for testing ##################
		print("in ask_streaming")
		print("camera flag")
		print(self.camera_execute_flag)
		#################################


		# if camera module is not used
		# execute streaming service
		if self.camera_execute_flag == -1:
			self.camera_execute_flag = 1
			print(self.camera_execute_flag)
			camera.view_stream()
	
		# if camera module is used
		# send error message to Server and return error code -2
		else:
			print("sorry, camera module is used")
			return -2
		print("exit to streaming")
		print(self.camera_execute_flag)

		# for testing ##################
		print("out ask_streaming")
		################################
	

		
	# ask for pir_sensor module,
	# execute pir_sensor module after status check
	def ask_pir_sensor(self):

		# for testing ###################
		print("in ask_pir_sensor")
		print("pir_sensor flag")
		print(self.pir_execute_flag)
		print("camera_sensor flag")
		print(self.camera_execute_flag)
		#################################

		# if camera module is used
		# send error message to Server and return error code -3
		if self.camera_execute_flag == 1:
			print("camera used for streaming service. You don't executed pir_sensor!")
			return -3
	
	
		# if camera moudl is not used
		# execute pir_sensor
		else:
			self.pir_execute_flag = 1
			pir_sensor.sensoring()
			self.pir_execute_flag = -1

		# for testing #################
		print("out ask_pir_sensor")
		###############################
