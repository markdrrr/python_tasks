#  Дан словарь. Добавить каждому ключу число равное длине этого ключа
# решение №1
dictionary = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
print(dictionary)
for key in list(dictionary.keys()):  # проходим циклом по списку ключей
    dictionary[f'{key}{len(key)}'] = dictionary.pop(key)
print(dictionary)

# решение №2
new_dictionary = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
print(new_dictionary)
i = 0  # счетчик для цикла
keys = list(new_dictionary.keys())  # список ключей
while i < len(keys):
    new_dictionary[f'{keys[i]}{len(keys[i])}'] = new_dictionary.pop(keys[i])
    i += 1
print(new_dictionary)
