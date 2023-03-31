# WanderlustNCL: Not all those who wander are lost
![WhatsApp Image 2023-03-29 at 4 59 17 PM](https://user-images.githubusercontent.com/75878788/228602856-99d7282c-331a-4257-8de6-ccb3a4b8612e.jpeg)

## Table of Contents
* [About](#about)
* [Technologies](#technologies)
* [Setup](#setup)
* [License](#license)

## About
WanderlustNCL is a tourism system that enhances the experience of visitors to Newcastle by creating walkable trails, revealing hidden gems, and facilitating souvenir collections. The project seeks to utilise the physical product by utilising the existing kiosks and introducing physical machines to assist users along the route without requiring mobile devices. In this pictorial, we present the design of the ecosystem of WanderlustNCL and explore the development and rationale behind the concept, as well as potential alternatives, through group brainstorming. This was followed by the production of initial prototypes and functional models. Throughout this process, we propose that our design is a tourism ecosystem that would enrich the travel experiences of tourists and allow them to immerse themselves in the local community.
![user](https://user-images.githubusercontent.com/75878788/228607731-e02f22ee-6369-4a51-9496-c82464a7cbb1.gif)

[Demonstration Video](https://vimeo.com/811339250)

## Technologies
We have two main components Kiosk and Wonderbox:

### Kiosk
Hardware:
- Surface Pro as a display for the web app
- Servo Motor for imitating printer
- Micro:bit V2 for servo motor

Software:
- Webapp (HTML/CSS/JS)

### WanderBox
Hardware:
- Raspberry Pi 4
- Micro:bit V2 for Neo Pixel
- Arduino
- Mini LCD Display
- Stepper Motor
- Stepper Motor TB6600 Driver
- 8 Buttons

Software:
- Python program for QR Code, & Directions
- C++ code for stamping mechanism

## Setup
**To run web app:**

- Clone or download the kisosk folder on your local computer
- Open the web_app folder and double click on the index.html file will open in the default browser. 
- To open in particular browser, right click on the file and select the required browser to run the file.
- To edit the code, open the file in any dev environment or any text editor.

**To run Direction & Trail Code**

- Setup raspberry pi with speaker & a display
- Install Necessary modules

```python
sudo apt-get update
sudo apt-get install python3-rpi.gpio
sudo apt-get install python3-pygame
pip3 install gtts googlemaps
```
- Open terminal
- Run the following command to run "run.py"

```python
sudo python3 run.py
```

**To run Map code**
- Install the necessary dependencies

```python
sudo apt-get install python-rpi.gpio xdotool
```
- Run the script

```python
sudo python3 map.py
```

**To Run Stamp Code**
- Install Arduino IDE from [here](https://www.arduino.cc/en/software)
- Open the code in the Arduino IDE.
- Select the correct board and serial port from the Tools menu according to your arduino.
- Attach necessary componentsbutton, stepper motor & stepper motor driver to arduino.
- Click Upload button to upload the code on the board

## License
[MIT](https://choosealicense.com/licenses/mit/)
