import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

# Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 

    
def push10(event):
    print("Button 10 was pushed!")
    

def push12(event):
    print("Button 12 was pushed!")
    
def release12(event):
    print("Button 12 up.")
        
def push16(event):
    print("Button 14 was pushed!")
    
def release16(event):
    print("Button 14 up.")

    
GPIO.add_event_detect(10, GPIO.RISING, callback=push10, bouncetime=300)
#GPIO.add_event_detect(12, GPIO.RISING, callback=push12, bouncetime=300)
#GPIO.add_event_detect(16, GPIO.RISING, callback=push16, bouncetime=300)

GPIO.add_event_detect(12, GPIO.FALLING, callback=release12, bouncetime=300)
GPIO.add_event_detect(16, GPIO.FALLING, callback=release16, bouncetime=300)


while True:
    pass