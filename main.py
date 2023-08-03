import requests

city = input(str('Introduce a valid city: '))
api_key=''
units='metric'
url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}?'
r = requests.get(url)
content = r.json()

def temp_celsius():
  temperatures = []
  for element in content['list']:
      temp = element['main']['temp']
      temp_cel = temp - 273.15
      temperatures.append(temp_cel)
      int_numbs = [int(items) for items in temperatures]
  return int_numbs
  
def get_weather(city):
    temperatures = temp_celsius()
    with open('data.txt', 'a') as file:
        for item, temp in zip(content['list'], temperatures):
            file.write(f"{city}, {item['dt_txt']}, {temp}°C, {item['weather'][0]['description']}\n")
      
print(get_weather(city))
