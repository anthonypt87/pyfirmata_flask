import pyfirmata

ARDUINO_PORT = '/dev/tty.usbmodemfa131'

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
		pin.mode = 3
		pin.write(value)
