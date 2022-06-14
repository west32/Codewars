import argparse

def check_prime(n):
    if n<=3:
        return n > 1

    if n%2 == 0 or n%3 == 0:
        return False

    sqrt = int(n**0.5) + 1

    for divisor in range(5, sqrt, 2):
        if n % divisor == 0:
            return False

    return True

def check_numbers(numbers):
    for number in numbers:
        if check_prime(number):
            flag = "is"
        else:
            flag = "is not"
        print("%d %s a prime number." % (number, flag))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        "Check if specified numbers are prime numbers or not."
    )

    parser.add_argument(
        "numbers",
        metavar="N",
        type=int,
        nargs="+",
        help="""The numbers to check, separated by empty space.""",
    )


    arguments = parser.parse_args()
    numbers = arguments.numbers

    check_numbers(numbers)


