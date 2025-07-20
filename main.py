x = 6
y = 6

if x < y:
    print('Значение X меньше значения Y')
elif x == y:
    print('Значение X равно значению Y')
else:
    print('Значение X больше значения Y')


arr = [25, 21, 372, 12, 627, 552, 133, 782]
obj = {"name": "John", "lastname": "Doe"}

print('Тип данных переменной arr: ', type(arr))
print('Тип данных переменной obj: ', type(obj))

for i in arr:
    print(i)

arrLength = len(arr)
print(f'В массиве arr: {arrLength} значений')

for i in range(arrLength):
    print(f'Число {i+1}: {arr[i]}')
print()

#ПРАКТИКА: Создание таблицы умножения

for i in range(1, 11, 1):
    for j in range(1, 11, 1):
        print(f'{i * j:4}', end=' ')
    print()
print()

#ПРАКТИКА: Вывод только четных строк таблицы умножения

for i in range(1, 11, 1):
    if i % 2 == 0: #Проверка на четность значения i
        for j in range(1, 11, 1):
            print(f'{i * j:4}', end=' ')
        print()
print()

#ПРАКТИКА: Вывод таблицы умножения до запрашиваемого у пользователя числа

x = int(input('Введите число до которого необходимо сгенерировать таблицу умножения: '))
print()

for i in range(1, x, 1):
    for j in range(1, x, 1):
        print(f'{i * j:5}', end=' ')
    print()
print()