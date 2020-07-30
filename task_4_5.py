# Составить список чисел Фибоначчи содержащий 15 элементов.
num = int(input('Введите число '))
list_f = [num, num]
for i in range(15):  # решение №1
    list_f.append(list_f[i] + list_f[i+1])
print(*list_f)

num2 = int(input('Введите число '))
list_f2 = [num2, num2]
amount = 0
while amount < 15:  # решение №2
    list_f2.append(list_f2[amount] + list_f2[amount + 1])
    amount += 1
print(*list_f2)
