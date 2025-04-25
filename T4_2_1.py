import random

def binary_search(random_list, num):
    first = 0
    mid = len(random_list) // 2  # создаем среднюю точку
    last = len(random_list) - 1  # создаем последняя точку

    while random_list[mid] != num and first <= last:  # проверяет если число списка не равно искомому и последнее меньше первого
        if num > random_list[mid]:  # если наше число больше текущего
            first = mid + 1  # то мы прибавляем единице к индексу
        else:
            last = mid - 1  # иначе мы отнимаем единицу
        mid = (first + last) // 2
    if first > last:
        return -1
    else:
        return mid

random_list = [random.randint(0, 50) for _ in range(10)] # создаю список случайных чисел
random_list.sort() # сортируем список
print("Список случайных чисел:", random_list)  #Вывод списка для отладки
num = random_list[random.randint(0, len(random_list) - 1)] # случайный элемент из списка для поиска
print("Искомое число:", num)  #Вывод списка для отладки
#num = 50
print (f'Искомое число находится на {binary_search(random_list, num)} месте')
