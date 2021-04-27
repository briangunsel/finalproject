from flask import Flask, render_template, request
import requests

app = Flask(__name__)

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=448b70adb1d3433eeac315494806c220&units=imperial'

@app.route('/')
def main():
	return render_template('index.html')

@app.route('/results', methods=['POST'])
def show_city():
	city = request.form['city_input']
	if requests.get(url.format(city)):
		source = requests.get(url.format(city)).json()
	else:
		return render_template('error.html', city=city)
	data = {
		'city': city.capitalize(),
		'temp': source['main']['temp'],
		'feels_like': source['main']['feels_like'],
		'temp_max': source['main']['temp_max'],
		'temp_min': source['main']['temp_min'],
		'description': (source['weather'][0]['description']).capitalize(),
		'wind_speed': source['wind']['speed'],
		'icon': source['weather'][0]['icon'],
		'country': source['sys']['country']
	}
	if city: 
		return render_template('city.html', data=data)
	
if __name__ == '__main__':
	app.run(debug=True)