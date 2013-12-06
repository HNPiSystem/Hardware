import camera
import pir_sensor
import send_email

class HardwareManager():

	# flag-> -1 : no use / 1 : use
	pir_execute_flag = -1
	camera_execute_flag = -1

	image_path = ''

	# initialize
	def __init__(self):

		# use global variables
		global pir_execute_flag
		global camera_execute_flag
		# for testing ################
		print("in init")
		##############################

	# get flag value #####################
	def get_camera_flag(self):
		return camera_execute_flag
	
	def get_pir_flag(self):
		return pir_execute_flag
	######################################

	# get imagefile_path #################
	def get_image_path(self):
		return image_path
	######################################

	# return to init flag ################
	def return_camera_flag(self):
		self.camera_execute_flag = -1
	
	def return_pir_flag(self):
		self.pir_execute_flag = -1
	######################################



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
	

	# quit to streaming service module
	#def ask_exit_streaming(self):
	#	print("testing...")
	#	self.camera_execute_flag = -1

		
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
