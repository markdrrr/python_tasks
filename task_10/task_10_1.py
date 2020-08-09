"""Создать csv файл с данными следующей структуры: Имя, Фамилия, Возраст.
Создать отчетный файл с информацией по количеству людей входящих в ту или иную возрастную группу.
Возрастные группы: 1-12, 13-18, 19-25, 26-40, 40+"""

# создаем файл
ppl = ['Иванов, Иван, Иванович, 23', 'Сидоров, Семен, Семенович, 23',
       'Яшков, Илья, Петрович, 24', 'Петрова, Галина, Ивановна, 55']
with open('../people.cvs', 'w') as my_file:
    for str_line in ppl:
        my_file.write(str_line + '\n')

old_ppl = []
with open('../people.cvs') as my_file:
    for line in my_file.readlines():
        s = line.replace("\n", "")
        old_ppl.append(s)

# создаем отсортированный файл
age_list = {'1-12': (1, 12), '13-18': (13, 18), '19-25': (19, 25), '26-40': (26, 40), '40+': (40, 150)}
with open('../sorted.cvs', 'w') as sorted:
    sorted.write('Возрастные группы:\n')

    for age in list(age_list.keys()):
        sorted.write(f'{age}:\n')
        for person in old_ppl:
            info_person = person.split(',')
            if age_list[age][0] <= int(info_person[3]) <= age_list[age][1]:
                sorted.write(f'{person}\n')
print('sorted')
