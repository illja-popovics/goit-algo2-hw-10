import random
import time
import matplotlib.pyplot as plt

# Рандомізований QuickSort
def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return randomized_quick_sort(less) + equal + randomized_quick_sort(greater)

# Детермінований QuickSort (опорний елемент - останній)
def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return deterministic_quick_sort(less) + equal + deterministic_quick_sort(greater)

# Генерація тестових даних
def generate_arrays(sizes):
    return {size: [random.randint(0, 1000000) for _ in range(size)] for size in sizes}

# Вимірювання часу виконання алгоритмів
def measure_time(algorithm, arrays):
    results = {}
    for size, array in arrays.items():
        times = []
        for _ in range(5):
            arr_copy = array.copy()
            start_time = time.time()
            algorithm(arr_copy)
            end_time = time.time()
            times.append(end_time - start_time)
        results[size] = sum(times) / len(times)
    return results

# Основна програма
sizes = [10_000, 50_000, 100_000, 500_000]
test_arrays = generate_arrays(sizes)

randomized_times = measure_time(randomized_quick_sort, test_arrays)
deterministic_times = measure_time(deterministic_quick_sort, test_arrays)

# Виведення результатів у термінал
for size in sizes:
    print(f"Розмір масиву: {size}")
    print(f"   Рандомізований QuickSort: {randomized_times[size]:.4f} секунд")
    print(f"   Детермінований QuickSort: {deterministic_times[size]:.4f} секунд")

# Побудова графіка
plt.figure(figsize=(8, 6))
plt.plot(sizes, list(randomized_times.values()), label="Рандомізований QuickSort", marker='o')
plt.plot(sizes, list(deterministic_times.values()), label="Детермінований QuickSort", marker='o')
plt.title("Порівняння рандомізованого та детермінованого QuickSort")
plt.xlabel("Розмір масиву")
plt.ylabel("Середній час виконання (секунди)")
plt.legend()
plt.grid()
plt.show()
