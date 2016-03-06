import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
motor = 4
led = 14
led1 = 26
led2 = 21
sensor = 20
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(motor, GPIO.OUT)
GPIO.setup(led, GPIO.OUT)
toara = GPIO.input(sensor)
toabans = toara
print '  esperant sensor'
while toara == toabans:
	toabans = toara
	toara = GPIO.input(sensor)
print '  intermitent inici'
for intermitent_inici in range(0, 2):
    print '\t',intermitent_inici
    GPIO.output(led, 1)
    time.sleep(0.5)
    GPIO.output(led, 0)
    time.sleep(0.5)
GPIO.output(led, 1)
GPIO.output(motor, 1)
print '  intermitent'
for intermitent in range(0, 20):
    print '\t',intermitent
    GPIO.output(led1, 1)
    GPIO.output(led2, 0)
    time.sleep(0.9)
    GPIO.output(led1, 0)
    GPIO.output(led2, 1)
    time.sleep(0.9)
print '  intermitent intermig'
for intermitent_intermig in range(0, 2):
    print '\t',intermitent_intermig
    GPIO.output(led, 0)
    GPIO.output(led1, 1)
    GPIO.output(led2, 0)
    time.sleep(0.9)
    GPIO.output(led1, 0)
    GPIO.output(led2, 1)
    GPIO.output(led, 1)
    time.sleep(0.9)
GPIO.output(led1, 1)
GPIO.output(led2, 0)
GPIO.output(motor, 0)
GPIO.output(led, 1)
GPIO.output(led1, 0)
GPIO.output(led2, 0)
print '  intermitent final'
for intermitent_final in range(0, 2):
    print '\t',intermitent_final	
    GPIO.output(led, 1)
    time.sleep(0.5)
    GPIO.output(led, 0)
    time.sleep(0.5)
GPIO.cleanup()
