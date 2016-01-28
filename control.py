import time
import os
import RPi.GPIO as GPIO

esc = 7
servo = 11

speedFile = os.getcwd() + "/speed.txt"
directionFile = os.getcwd() + "/direction.txt"

GPIO.setmode (GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(esc,GPIO.OUT)
GPIO.setup(servo,GPIO.OUT)
	
GPIO.setup(esc, GPIO.OUT)
escSignal = GPIO.PWM(esc, 50)
escSignal.start(6.8)

def getFileContent(path):
	fileContent = open(path, 'r')
	z = fileContent.read()
	fileContent.close()
	return z

time.sleep(2)
escSignal.ChangeDutyCycle(getFileContent(speedFile))
directionSignal = GPIO.PWM(servo,50)
directionSignal.start(getFileContent(directionFile))

while True:
	speed  = getFileContent(speedFile)
	direction  = getFileContent(directionFile)
	print escSignal
	escSignal.ChangeDutyCycle(speed)
	directionSignal.ChangeDutyCycle(direction)
	print "Speed "+ str(speed) + "\nDirection "+ str(direction) + "\n\n"
	time.sleep(0.1)

escSignal.stop()
direction.stop()
GPIO.cleanup()
