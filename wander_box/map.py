import subprocess # import the subprocess module for spawning new processes
import time # import the time module for handling sleep operations
import RPi.GPIO as GPIO # import the GPIO module for interfacing with the Raspberry Pi's GPIO pins

image_viewer_process = None # initialize a variable to hold the process of the image viewer

def on_button_pressed(channel): # define a function to be called when the button is pressed
    global image_viewer_process # use the global variable to track the image viewer process
    
    if image_viewer_process is None: # if the image viewer is not running
        image_viewer_process = subprocess.Popen(['xdg-open', '/home/pi/Desktop/Scanner/map.jpg']) # open the image viewer process and store it in the global variable
        time.sleep(2) # wait for the window to open
        image_viewer_process.poll() # check the status of the image viewer process
        if image_viewer_process.returncode is None: # if the image viewer process is still running
            # maximize the window if it is still open
            subprocess.run(['xdotool', 'search', '--name', 'map.jpeg', 'windowactivate', '--sync', 'key', 'F11']) # use the xdotool utility to maximize the window
    else: # if the image viewer is already running
        # bring the window out of full screen mode
        subprocess.run(['xdotool', 'search', '--name', 'map.jpeg', 'windowactivate', '--sync', 'key', 'F11']) # use xdotool to restore the window to normal size
        time.sleep(1) # wait for the window to exit full screen mode
        # close the window
        subprocess.run(['xdotool', 'search', '--name', 'map.jpeg', 'windowactivate', '--sync']) # activate the window
        time.sleep(1) # wait for the window to activate
        subprocess.run(['xdotool', 'key', 'Escape']) # simulate the Escape key to close the window
        image_viewer_process.terminate() # terminate the image viewer process
        image_viewer_process.wait() # wait for the process to exit
        image_viewer_process = None # set the global variable to None to indicate that the process has been terminated

GPIO.setmode(GPIO.BCM) # set the mode of the GPIO library to BCM
GPIO.setwarnings(False) # disable GPIO warnings
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP) # configure the GPIO pin for input and enable the pull-up resistor
GPIO.add_event_detect(21, GPIO.FALLING, callback=on_button_pressed, bouncetime=5000) # add an event detection for a falling edge on the GPIO pin

while True: # start an infinite loop
    try:
        time.sleep(1) # wait for 1 second
    except KeyboardInterrupt: # if the user presses Ctrl+C
        GPIO.cleanup() # clean up the GPIO resources
        break # exit the loop
