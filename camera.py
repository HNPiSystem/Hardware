import os
import sys
import time

set_device_video = "uv4l --driver raspicam --auto-video_nr --framerate 25"


def camera_execute():

	now = time.localtime()
	filename = str(now.tm_year)+str(now.tm_mon)+str(now.tm_mday)+'-'+str(now.tm_hour)+str(now.tm_min)+str(now.tm_sec)

        if not os.path.exists("/dev/video0"):
                print("video device is not found")
                os.system(set_device_video)
        else:
                print("video device is exist")

	os.system('raspistill -o ./static/' + filename + '.jpg')

	import get_ip
	return 'http://' + get_ip.get_ip_address('eth0') + ':5000/static/' + filename + '.jpg'

def view_stream():

	video_stream = "cvlc v4l2:///dev/video0 --v4l2-width 640 --v4l2-height 480 --v4l2-chroma h264 --sout '#rtp{sdp=rtsp://:8554/}'"

	if not os.path.exists("/dev/video0"):
		print("video device is not found")
		os.system(set_device_video)
	else:
		print("video device is exist")
	
	os.system(video_stream)
