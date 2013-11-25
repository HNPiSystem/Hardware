import os
import sys
import time

def camera_execute():

	now = time.localtime()
	filename = str(now.tm_year)+str(now.tm_mon)+str(now.tm_mday)+'-'+str(now.tm_hour)+str(now.tm_min)+str(now.tm_sec)

	os.system('raspistill -o ./static/' + filename + '.jpg')

	#print filename
	return 'http://192.168.0.4:5000/static/' + filename + '.jpg'

def get_path(filename):
	path =  'http://192.168.0.4:5000/' + filename + '.jpg'
	#print path
	return path	

#get_path(camera_execute())

def view_stream():
	os.system("cvlc v4l2:///dev/video2 --v4l2-width 640 --v4l2-height 480 --v4l2-chroma h264 --sout \'#rtp{sdp=rtsp://8554/}\'")
	#print command

view_stream()
