from arduino import Arduino
from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)

@app.route('/flashing_lights')
def flashing_lights():
	return render_template(
		'flashing_lights.html', 
	)

@app.route('/flashing_lights/update_color/<hex_color>')
def update_color(hex_color):
	prepared_arduino_values = _get_prepared_rgb_tuple_for_arduino(hex_color)
	arduino = Arduino()
	arduino.set_rgb_value(prepared_arduino_values)
	return 'success'

def _get_prepared_rgb_tuple_for_arduino(hex_color):
	assert len(hex_color) == 6
	hexes = hex_color[:2], hex_color[2:4], hex_color[4:]
	return  [int(hex_value, 16)/256.0 for hex_value in hexes]

@app.route('/on/<pin>')
def on(pin):
	arduino = Arduino()
	arduino.digital_turn_on(int(pin))
	return 'on'

@app.route('/off/<pin>')
def off(pin):
	arduino = Arduino()
	arduino.digital_turn_off(int(pin))
	return 'off'

if __name__ == '__main__':
	app.run(debug=True)
