from fizzbuzz_testing import __version__
from fizzbuzz_testing.fizzbuzz import fizzbuzz


def test_version():
    assert __version__ == "0.1.0"


def test_fizz():
    input_list = [3, 6, 9, 12]
    for inpt in input_list:
        assert fizzbuzz(inpt) == "Fizz"


def test_buzz():
    input_list = [5, 10, 20]
    for inpt in input_list:
        assert fizzbuzz(inpt) == "Buzz"


def test_fizzbuzz():
    input_list = [15, 30]
    for inpt in input_list:
        assert fizzbuzz(inpt) == "FizzBuzz"
