import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

# Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 

led_pin = 32
GPIO.setup(led_pin, GPIO.OUT)

    
def push10(channel):
    print("Button 10 was pushed!")
    GPIO.output(led_pin, GPIO.LOW)
    exit()

def push12(channel):
    print("Button 12 was pushed!")
    GPIO.output(led_pin, GPIO.HIGH)
            
def push16(channel):
    if GPIO.input(channel):
        GPIO.output(led_pin, GPIO.HIGH)
        print("Button 14 was pushed!")
    else:
        GPIO.output(led_pin, GPIO.LOW)
        print("Button 14 was released!")

    
GPIO.add_event_detect(10, GPIO.RISING, callback=push10, bouncetime=300)
GPIO.add_event_detect(12, GPIO.RISING, callback=push12, bouncetime=300)
GPIO.add_event_detect(16, GPIO.BOTH, callback=push16, bouncetime=30)

# can only be up OR down, not both
# GPIO.add_event_detect(12, GPIO.FALLING, callback=release12, bouncetime=300)
# GPIO.add_event_detect(16, GPIO.FALLING, callback=release16, bouncetime=300)


while True:
    pass