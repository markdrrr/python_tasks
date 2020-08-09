"""Дан файл, содержащий различные даты.
Каждая дата - это число, месяц и год. Найти самую раннюю дату."""
from datetime import datetime

# создаем файл
ppl = ['09.08.2020', '03.08.2020', '05.06.2020', '09.07.2020', '09.02.2020', '02.08.2020', '19.03.2020']
with open('date.cvs', 'w') as my_file:
    for str_line in ppl:
        my_file.write(str_line + '\n')
# читаем файл
date_list = []
with open('date.cvs') as my_file:
    for line in my_file.readlines():
        s = line.replace('\n', '')
        date_list.append(s)
first_day = datetime.strptime(date_list[0], '%d.%m.%Y')
for date in date_list:
    day = datetime.strptime(date, '%d.%m.%Y')
    if day < first_day:
        first_day = day
print(date_list)
print('Самая ранняя дата:', first_day.strftime("%d.%m.%Y"))
