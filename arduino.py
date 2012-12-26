import pyfirmata

ARDUINO_PORT = '/dev/tty.usbmodemfd121'
PWM_MODE = 3

RED_PIN = 6
GREEN_PIN = 5
BLUE_PIN = 3

# Singleton implementation from PEP318
def singleton(cls):
	instances = {}
	def getinstance():
		if cls not in instances:
			instances[cls] = cls()
		return instances[cls]
	return getinstance

@singleton
class Arduino(object):

	def __init__(self, port=None):
		self.board = pyfirmata.Arduino(ARDUINO_PORT)
	
	def digital_turn_on(self, pin_number):
		self.board.digital[pin_number].write(1)

	def digital_turn_off(self, pin_number):
		self.board.digital[pin_number].write(0)

	def set_pwm_value(self, pin_number, value):
		pin = self.board.digital[pin_number]
		pin.mode = PWM_MODE
		pin.write(value)

	def set_rgb_value(self, rgb_tuple):
		for pin, value in zip((RED_PIN, GREEN_PIN, BLUE_PIN), rgb_tuple):
			self.set_pwm_value(pin, value)
		
