'''
3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся
элементов исходной последовательности.
'''
myList = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {myList}\n")
newList = []
[newList.append(i) for i in myList if i not in newList]
print(f"Список из неповторяющихся элементов: {newList}\n")