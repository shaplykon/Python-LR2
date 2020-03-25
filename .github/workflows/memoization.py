import random


def memoization(function):
    cache = {}

    def decorate(*args):
        if args in cache:
            print("Decorator worked!")
            return cache[args]
        else:
            cache[args] = function(*args)
            return cache[args]

    return decorate


@memoization
def squaring(x):
    return pow(x, 2)


def main():
    for i in range(100):
        x = random.randint(0, 10)
        print(i + 1, ": ", x, "^2 = ", squaring(x))


if __name__ == "__main__":
    main()
