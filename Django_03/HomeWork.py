def fibonacci_generator():
    first = 0
    second = 1

    while True:
        yield first
        first, second = second, first + second


generator = fibonacci_generator()

for _ in range(10):
    print(next(generator))
