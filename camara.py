import os
import sys
import time

def camera():

	now = time.localtime()
	name = str(now.tm_year)+str(now.tm_mon)+str(now.tm_mday)+'-'+str(now.tm_hour)+':'+str(now.tm_min)+':'+str(now.tm_sec)

	execute_camera = os.system('raspistill -o ' + name + '.jpg')

	print name
	return name

camera()
