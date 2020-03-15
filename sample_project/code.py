import re

"""
1.


   1. The method can take 0, 1 or 2 numbers, and will
   return their sum (for an empty string it will return 0)
   for example
   `“” == 0 , “1” == 1 , “1,2” == 3`
"""
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

"""


class StringCalculator:
    def add(numbers: str) -> int:
        def find_numbers(str_nums):
            if str_nums[0] == "/":
                pattern = rf"[{str_nums[2]},\n]"
                return re.split(pattern, str_nums)
            else:
                return re.split(r"[,\n]", str_nums)

        def sum_numbers(list_str_nums):
            sum_of_numbers = 0

            for num in list_str_nums:
                if num.isdigit():
                    sum_of_numbers += int(num)
            return sum_of_numbers

        while len(numbers) > 1:
            list_strings = find_numbers(numbers)
            return sum_numbers(list_strings)
        else:
            return 0 if numbers == "" else int(numbers[0])
