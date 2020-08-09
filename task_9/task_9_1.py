""" Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’,
 где i это порядковый номер строки в списке. Использовать генератор списков. """

words = ['hello', 'goodbye', 'how are you']
print(words)
new_list = [f'{i + 1} - {words[i]}' for i in range(len(words))]
print(new_list)
