import time
import serial
import string
import pynmea2
import RPi GPIO as gpio
import Adafruit_CharLCD as LCD
gpio.setmode(gpio.BCM)
GPIO.setup(11, GPIO.IN)   
GPIO.setup(3, GPIO.OUT)         
ser = serial.Serial(port, baudrate = 9600, timeout = 0.5)
alertdriver():
while 1:
    try:
        data = ser.readline()
    except:
print("loading")  
    if data[0:6] == '$GPGGA':
        msg = pynmea2.parse(data)
        latval = msg.lat
concatlat = "lat:" + str(latval)
        print concatlat    #printing the latitude
lcd.set_cursor(0,0)
lcd.message(concatlat)
longval = msg.lon
concatlong = "long:"+ str(longval)
print concatlong     # printing the longtitude
i=GPIO.input(11)
if i==1:               
print "seat filled by the passenger",i  #printing the seat occupaied or not
    time.sleep(0.5)




def  alertdriver():
TRIG =3
ECHO =5
While(1):
print "Distance measurement in progress“
GPIO.setmode(GPIO.BOARD)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.output(TRIG,False)
print "Waiting for sensor to settle down"
time.sleep(2)
GPIO.output(TRIG,True)
time.sleep(0.00001)
GPIO.output(TRIG,False)
while GPIO.input(ECHO)==0:
Pulse_start=time.time()
while GPIO.input(ECHO)==1:
Pulse_end=time.time()
Pulse_duration= Pulse_end - Pulse_start
distance = Pulse_duration*17150
distance=round(distance,2)
print "Distance : " ,distance ,"Cm“
if Distance<10
GPIO.output(7,True) 	#alert the driver
 time.sleep(5)
GPIO.output(7,false)	#reset the alert signal
GPIO.cleanup()
 
 


