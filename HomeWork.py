import random

# Задание 1

my_list =[]
for i in range(15):
    my_list.append(random.randint(-50, 50))

print("Сгенерированный список:", my_list)

p_count = 0
n_count = 0
z_count = 0

positives = []
negatives =[]

for i in range(len(my_list)):
    if my_list[i] > 0:
        p_count += 1
        positives.append(my_list[i])
    elif my_list[i] < 0:
        n_count += 1
        negatives.append(my_list[i])
    else:
        z_count += 1

print("-" * 20)

if p_count > 0:
    print(f"Минимальное положительное число: {min(positives)}")
if n_count > 0:
    print(f"Максимальное отрицательное число: {max(negatives)}")

print(f"Кол-во положительных: {p_count}")
print(f"Кол-во отрицательных: {n_count}")
print(f"Кол-во нулей: {z_count}")


print("\n" + "=" * 40 + "\n")


# Задание 2

numbers = list(map(int, input("Введите список чисел через пробел: ").split()))
number = int(input("Введите число: "))

for num in numbers[:]:
    if num < number:
        numbers.remove(num)

print("Результат:", numbers)