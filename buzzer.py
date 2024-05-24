import RPi.GPIO as GPIO
import time

# Disable warnings
GPIO.setwarnings(False)

# Set GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define GPIO pins
PIR_PIN = 11  # Connected to SPISCLK
LED_PIN = 26  # Connected to GPIO19
BUZZER_PIN = 8  # Connected to SPI0 CE0

# Set up GPIO pins: PIR sensor as input, LED and buzzer as output
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# Function to activate buzzer and LED
def activate_alarm():
    GPIO.output(LED_PIN, GPIO.HIGH)  # Turn on LED
    GPIO.output(BUZZER_PIN, GPIO.HIGH)  # Turn on buzzer
    time.sleep(1)  # Wait for 1 second
    GPIO.output(LED_PIN, GPIO.LOW)  # Turn off LED
    GPIO.output(BUZZER_PIN, GPIO.LOW)  # Turn off buzzer

try:
    # Continuous loop to monitor for motion
    while True:
        # Check if there is movement detected by the PIR sensor
        if GPIO.input(PIR_PIN):
            # If motion is detected, activate the alarm
            activate_alarm()
            print("Motion detected!")

        # Add a small delay to reduce CPU usage
        time.sleep(0.1)

except KeyboardInterrupt:
    # Clean up GPIO settings on keyboard interrupt
    GPIO.cleanup()
