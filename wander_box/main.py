# Import necessary modules
import RPi.GPIO as GPIO # For controlling Raspberry Pi's GPIO pins
import time
import os # For interacting with the operating system
from gtts import gTTS # For text-to-speech conversion
from pygame import mixer # For playing audio files
import googlemaps # For interacting with Google Maps API
import re # For text processing
import getpass # For getting user input without echoing it on the console

# Function to clear the console screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Set up text-to-speech
mixer.init()

# Location list
locations = []

# Get location list from console input
location_string = getpass.getpass(prompt="Please scan the QR code." + '\n')
locations = location_string.split(';')
# clear_screen()

# Remove any leading or trailing whitespace from each location
for i in range(len(locations)):
    locations[i] = locations[i].strip()

# Get Google Maps API key
# Replace <API KEY> With your google api key
api_key = "<API KEY>"

# Initialize Google Maps client
gmaps = googlemaps.Client(key=api_key)

# Set up GPIO pins for the custom buttons
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button 1, connected to GPIO2
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button 2, connected to GPIO3
GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Button 3, connected to GPIO4
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button 4, connected to GPIO14
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button 5, connected to GPIO15


# Loop to get directions from the selected location
while True:
    # Print the location list
    print('\n')
    for i, location in enumerate(locations):
        newLoc = location
        updatedLoc = newLoc.replace("newcastle", "") # Remove the word 'newcastle' from the location name
        print(str(i+1) + ". " + updatedLoc.upper()) # Print the updated location name in uppercase

    # Ask the user to select a location
    print('\n' + "Press a button to select a location: ")
    selection = None
    originLoc = ""
    
    while selection is None:
        # Check which button was pressed
        if not GPIO.input(15): # Button 1
            selection = 1
            print("Button 1")
        elif not GPIO.input(17): # Button 2
            selection = 2
            print("Button 2")
        elif not GPIO.input(2): # Button 3
            selection = 3
            print("Button 3")
        elif not GPIO.input(18): # Button 4
            selection = 4
            print("Button 4")
        elif not GPIO.input(14): # Button 5
            selection = 5
            print("Button 5")

        # Validate the selection
        if selection is not None and (selection < 1 or selection > len(locations)):
            clear_screen() # Clears screen
            print("Invalid selection. Please press a button between 1 and", len(locations)) # Print Invalid selection message
            selection = None 

    print("Selection: ", selection)  # Print the selected location index
    destination = locations[selection-1]  # Get the selected destination location from the locations list
    origin = '51.5007042,-0.1245721'  # Set the current location as a string value
    directions_result = gmaps.directions(origin, destination, mode='walking')  # Get the directions from current to selected location
    steps = directions_result[0]['legs'][0]['steps']  # Get the directions steps from the directions result

    # Speak out and display the direction
    selection = None  # Reset the selection variable to None
    clear_screen()  # Clear the screen
    print('\n' + "Directions:")  # Print a heading for the directions
    first_step = steps[0]  # Get the first step of the directions
    directions = re.sub('<[^<]+?>', '', first_step['html_instructions'])  # Remove HTML tags from the directions
    print(directions + '\n')  # Print the directions

    # Speak the directions using text-to-speech
    tts = gTTS(text=directions, lang='en', tld='co.uk')  # Create a text-to-speech object with the directions
    tts.save('direction.mp3')  # Save the text-to-speech as an MP3 file
    mixer.music.load('direction.mp3')  # Load the MP3 file
    mixer.music.play()  # Play the MP3 file

    # Wait for the text-to-speech to finish speaking before moving on
    while mixer.music.get_busy():
        time.sleep(0.1)


