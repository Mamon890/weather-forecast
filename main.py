import requests

s_city = input("Введите город: ")
appid = "###"

res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                   params={'q': s_city,'units':'metric','lang':'ru','APPID': appid})
data = res.json()

print('Сейчас:')
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура", data['main']['temp_max'])
print("Скорость ветра:", data['wind']['speed'])
print("Видимость:", data['visibility'])

res = requests.get("http://api.openweathermap.org/data/2.5/forecast", params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()

print("\n\nПрогноз погоды на неделю: \n____________________________")
for i in data['list']:
    print("Дата:", i['dt_txt'], "\nТемпература:", '{0:+3.0f}'.format(i['main']['temp']), "\nПогодные условия:", i['weather'][0]['description'], "\nСкорость ветра:", i['wind']['speed'], "\nВидимость:", i['visibility'])
    print("____________________________")
