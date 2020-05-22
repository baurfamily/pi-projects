import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

# Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 


pushed10 = False
pushed12 = False
pushed16 = False

while True: # Run forever
    if GPIO.input(10) == GPIO.HIGH and not pushed10:
        pushed10 = True
        print("Button 10 was pushed!")
    elif GPIO.input(10) == GPIO.LOW and pushed10:
        pushed10 = False
        print("Button 10 up.")
        
    if GPIO.input(12) == GPIO.HIGH and not pushed12:
        pushed12 = True
        print("Button 12 was pushed!")
    elif GPIO.input(12) == GPIO.LOW and pushed12:
        pushed12 = False
        print("Button 12 up.")
        
    if GPIO.input(16) == GPIO.HIGH and not pushed16:
        pushed16 = True
        print("Button 14 was pushed!")
    elif GPIO.input(16) == GPIO.LOW and pushed16:
        pushed16 = False
        print("Button 14 up.")