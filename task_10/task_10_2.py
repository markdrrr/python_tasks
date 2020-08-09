"""Создать csv файл с данными о ежедневной погоде.
Структура:  Дата, Место, Градусы, Скорость ветра.
Найти среднюю погоду(скорость ветра и градусы) для Минск за последние 7 дней. """

# создаем файл
ppl = ['09.08.2020, Москва, +22, 3м/с', '08.08.2020, Москва, +17, 11м/с',
       '07.08.2020, Москва, +23, 25м/с', '06.08.2020, Москва, +28, 10м/с',
       '05.08.2020, Москва, +31, 23м/с', '04.08.2020, Москва, +15, 4м/с',
       '03.08.2020, Москва, +14, 1м/с']
with open('weather.cvs', 'w') as my_file:
    for str_line in ppl:
        my_file.write(str_line + '\n')
# читаем файл
weather_list = []
with open('weather.cvs') as my_file:
    for line in my_file.readlines():
        s = line.replace("\n", "")
        weather_list.append(s)
print(weather_list)
sum_tmp = 0
for day in weather_list:
    sum_tmp += int(day.split(',')[2])
midle = (lambda x: f'+{x}' if x > 0 else f'{x}')(round(sum_tmp/len(weather_list)))  # ставим + или - перед цифрой
print(f'Средняя темпиратура {midle} градус за последнии {len(weather_list)} дней')
