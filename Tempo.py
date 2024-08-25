import requests

# Substitua 'your_api_key' pela sua chave da API
API_KEY = '1170d79a047eeed2c944f482cf5c2956'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city_name):
    url = f"{BASE_URL}?q={city_name}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        print(f"Cidade: {city_name}")
        print(f"Temperatura: {main['temp']}°C")
        print(f"Clima: {weather['description']}")
        print(f"Umidade: {main['humidity']}%")
        print(f"Pressão: {main['pressure']} hPa")
    else:
        print("Cidade não encontrada ou erro na API.")

if __name__ == "__main__":
    city = input("Digite o nome da cidade: ")
    get_weather(city)
