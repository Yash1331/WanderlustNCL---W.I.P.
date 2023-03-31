import os
import subprocess
import time

# Set the timeout period (in seconds)
TIMEOUT = 120

while True:

    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Run main.py program as a subprocess
    process = subprocess.Popen(["python3", "main.py"])

    # Wait for TIMEOUT seconds
    time.sleep(TIMEOUT)

    # Terminate the subprocess
    process.terminate()
    
