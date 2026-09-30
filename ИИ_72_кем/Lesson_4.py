# я сделал не через if else

weather_conditions = ["sunny", "cloudy", "rainy", "snowy"]
weather_conditions2 = {"1": "You should wear T-shirt and shorts",
                      "2": "You should wear coat and trousers",
                      "3": "You should wear raincoat",
                      "4": "You should wear jacket and thick trousers"}

menu = f"Please select weather condition\n"
for i in range(len(weather_conditions)):
    menu += f"{str(i+1)} - {weather_conditions[i]}\n"
menu += f"> "

user_weather = str(input(menu))

if weather_conditions2.get(user_weather) == None:
    print("Oh, I don't know what you should to wear")
else:
    print(weather_conditions2.get(user_weather))
