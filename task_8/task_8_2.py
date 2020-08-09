""" Даны три слова. Выяснить, является ли хоть одно из них палиндромом ("перевертышем"),
 т. е. таким, которое читается одинаково слева направо и справа налево. (Определить функцию,
 позволяющую распознавать слова палиндромы.)"""
words = ['нога', 'рука', 'топот']


def palidrom(list_words):
    pldr_list = []
    pldr = None
    for word in list_words:
        index = 0
        for char in word:
            if index < len(word) / 2 - 1:
                if char == word[-1 - index]:
                    pldr = word
                else:
                    pldr = None
                    break
            index += 1
        if pldr is not None:
            pldr_list.append(pldr)
    return pldr_list


print(words)
print(*palidrom(words))
