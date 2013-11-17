import os
import sys
import time

def camera_execute():

	now = time.localtime()
	filename = str(now.tm_year)+str(now.tm_mon)+str(now.tm_mday)+'-'+str(now.tm_hour)+':'+str(now.tm_min)+':'+str(now.tm_sec)

	os.system('raspistill -o ' + filename + '.jpg')

	print filename
	return filename

def get_path(filename):
	path = os.getcwd() + '/' + filename + '.jpg'
	print path
	return path	

get_path(camera_execute())
