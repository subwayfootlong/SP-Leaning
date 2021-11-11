#Lutfi Lais P1946853
#Muhammad Idris P1948363
#MRT Air-con control system
#When its temperature >26 aircon will turn on,if still >26 after 5 seconds, will send notification on twitter saying aircon spoil
#able to track temperature on thingspeak
#able to track temperature on webserver and also contact staff
import RPi.GPIO as GPIO
import dht11
import time
import datetime
import requests
import Adafruit_DHT
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

instance = dht11.DHT11(pin=21) #read data using pin 21
GPIO.setup(23,GPIO.OUT) #set GPIO 23 as output
GPIO.setup(22,GPIO.OUT) #set GPIO 22 as output
    
try:
    while True: #keep reading, unless keyboard is pressed
        result = instance.read()
        if result.is_valid(): #print datetime & sensor values
            print("Temperature: %-3.1f C" % result.temperature)
            resp=requests.get("https://api.thingspeak.com/update?api_key=XFT7RUIQG9A2L7UX&field1=%s" %result.temperature)
        if result.temperature>26 or GPIO.input(22) :
            GPIO.output(23,1) #output logic low/'1'
            print("motor on")
            time.sleep(5)
            result = instance.read()
            if result.temperature>26:
                resp = requests.post('https://api.thingspeak.com/apps/thingtweet/1/statuses/update',
                    json={'api_key':'UVY2Z5ECUKE2PST8','status': 'Aircon spoilt' })
                print("aircon spoiltt")
        if result.temperature<26:
            GPIO.output(23,0) #output logic low/'0'
            
        time.sleep(0.5) #short delay between reads

except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup() #Google what this means…
