# Import required Python libraries
import RPi.GPIO as GPIO
import time, tweet_push


def sensoring(): 
  # Use BCM GPIO references
  # instead of physical pin numbers
  GPIO.setmode(GPIO.BCM)
   
  # Define GPIO to use on Pi
  GPIO_PIR = 7
  GPIO_LED = 23
   
  print "PIR Module Test (CTRL-C to exit)"
   
  # Set pin as input
  GPIO.setup(GPIO_PIR,GPIO.IN)      # Echo
  GPIO.setup(GPIO_LED,GPIO.OUT)
   
  Current_State  = 0
  Previous_State = 0

  try:
   
    print "Waiting for PIR to settle ..."
   
    # Loop until PIR output is 0
    while GPIO.input(GPIO_PIR)==1:
      Current_State  = 0
   
    print "  Ready"
   
    # Loop until users quits with CTRL-C
    while True :

      # Read PIR state
      Current_State = GPIO.input(GPIO_PIR)

      if Current_State==1 and Previous_State==0:
        # PIR is triggered
        print "  Motion detected!"
	tweet_push.twitter_push()
        time.sleep(5)

	# LED turned on
        GPIO.output(GPIO_LED, True)
	
	#file_path = camera.camera_execute()	
        #send_email.send_gmail(file_path)

        # Record previous state
        Previous_State=1
        
      elif Current_State==0 and Previous_State==1:
        # PIR has returned to ready state
        print "  Ready"
        # LED turned off
        GPIO.output(GPIO_LED, False)
        Previous_State=0
 
      # Wait for 1 milliseconds
      time.sleep(5)


  except KeyboardInterrupt:
  	print " Quit"
  	# Rest GPIO settings
  	GPIO.cleanup()
