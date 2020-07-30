#  Дан словарь. Добавить каждому ключу число равное длине этого ключа
dictionary = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
print(dictionary)
for key in list(dictionary.keys()):  # проходим циклом по списку ключей
    dictionary[f'{key}{len(key)}'] = dictionary.pop(key)
print(dictionary)
