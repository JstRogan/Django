def apply_to_numbers(numbers, func):
    return [func(number) for number in numbers]


def even_numbers(numbers):
    for number in numbers:
        if number % 2 == 0:
            yield number


def running_total(numbers):
    total = 0
    for number in numbers:
        total += number
        yield total


def simple_logger(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов функции: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result

    return wrapper


@simple_logger
def multiply(a, b):
    return a * b


def main():
    numbers = [1, 2, 3, 4, 5, 6]

    squares = apply_to_numbers(numbers, lambda number: number ** 2)
    print("Квадраты чисел:", squares)

    print("Чётные числа:")
    for number in even_numbers(numbers):
        print(number)

    print("Накопительная сумма:")
    for total in running_total(numbers):
        print(total)

    multiply(4, 5)


if __name__ == "__main__":
    main()
