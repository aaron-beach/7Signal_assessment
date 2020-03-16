import re

"""
    create a simple class `class StringCalculator`
    with a method `public int Add(string numbers)`

    Methods:

    Add(numbers)
        receives numbers as string
        returns int

        Helper methods
        -   find_numbers(num)
                receives numbers as string
                returns list of strings
        -   sum_numbers(list_str_nums)
                receives list as strings
                returns int sum
"""


class StringCalculator:
    def __init__(self, count):
        self.count = count

    def GetCalledCount(self):
        self.count += 1
        return self.count

    @staticmethod
    def find_numbers(str_nums: str):
        if str_nums[0] == "/":
            pattern = re.compile("-?[0-9]+")
            return pattern.findall(str_nums, 4)
        else:
            return re.findall(r"-?[0-9]+", str_nums)

    @staticmethod
    def is_positive(num):
        if int(num) < 0:

            raise ValueError("negatives not allowed")

    @staticmethod
    def sum_numbers(list_str_nums):
        sum_of_numbers = 0
        for num in list_str_nums:
            try:
                StringCalculator.is_positive(num)
                if num.isdigit():
                    sum_of_numbers += int(num)
            except ValueError:
                print("negatives not allowed: " + num)
        return sum_of_numbers

    def add(self, numbers: str) -> int:
        StringCalculator.GetCalledCount(self)
        while len(numbers) > 1:
            list_strings = StringCalculator.find_numbers(numbers)
            return StringCalculator.sum_numbers(list_strings)
        else:
            return 0 if numbers == "" else int(numbers[0])


def main():
    calc = StringCalculator()
    calc.add("1,1")
    print(calc)


if __name__ == "__main__":
    main()
