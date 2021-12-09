def main():
    for i in range(1, 101):
        print(fizzbuzz(i))


def fizzbuzz(i: int) -> str:
    if i % 15 == 0:
        return "FizzBuzz"
    elif i % 3 == 0:
        return "Fizz"
    elif i % 5 == 0:
        return "Buzz"
    else:
        return str(i)


if __name__ == "__main__":
    main()
