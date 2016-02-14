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
	try:
		p = float(z)
	except ValueError:
		p = float(z)
	fileContent.close()
	return p
	
time.sleep(1)
escSignal.ChangeDutyCycle(getFileContent(speedFile))
directionSignal = GPIO.PWM(servo,50)
directionSignal.start(getFileContent(directionFile))

ec = 0
while True:
	try:
		speed  = getFileContent(speedFile)
	except ValueError:
		pass		
	try:
		direction  = getFileContent(directionFile)
	except ValueError:
		pass
	escSignal.ChangeDutyCycle(speed)
	if (direction != ec):
		print escSignal	
		directionSignal.ChangeDutyCycle(direction)
		print "Speed "+ str(speed) + "\nDirection "+ str(direction) + "\n\n"
		time.sleep(0.1)
		ec = getFileContent(directionFile)

escSignal.stop()
direction.stop()
GPIO.cleanup()
