import random
import matplotlib.pyplot as plt
import timeit


def linear_search(random_list, num):
    for i in range(len(random_list)):
        if random_list[i] == num:
            return i
    return -1

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

linear_times = []
binary_times = []
list_sizes = [10, 100, 500, 1000, 2000, 3000, 4000, 5000] # Размеры списков для тестирования

def binary_search_time():
    binary_search(random_list, num)

def linear_search_time():
    linear_search(random_list, num)

for range_list in list_sizes:
    random_list = [random.randint(0, 5000) for _ in range(range_list)] # создаю список случайных чисел
    num = random_list[random.randint(0, len(random_list) - 1)]  # случайный элемент из списка для поиска
    random_list.sort() # сортируем список

    linear_time = timeit.timeit(stmt=linear_search_time, number=100) # Измеряем время выполнения линейного поиска
    binary_time = timeit.timeit(stmt=binary_search_time, number=100) # Измеряем время выполнения бинарного поиска

    linear_times.append(linear_time) # заношу значения в список для графика
    binary_times.append(binary_time) # заношу значения в список для графика



# Строю график
plt.plot(list_sizes, linear_times, label="Линейный поиск")
plt.plot(list_sizes, binary_times, label="Бинарный поиск")
plt.xlabel("Размер списка")
plt.ylabel("Время выполнения (секунды)")
plt.title("Сравнение времени выполнения поиска")
plt.legend()
plt.grid(True)
plt.show()
