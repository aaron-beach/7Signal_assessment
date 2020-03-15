import re

"""
1.
    create a simple class `class StringCalculator`
    with a method `public int Add(string numbers)`

   1. The method can take 0, 1 or 2 numbers, and will
   return their sum (for an empty string it will return 0)
   for example
   `“” == 0 , “1” == 1 , “1,2” == 3`
"""


class StringCalculator:
    def add(number: str) -> int:

        """
        2. Start with the **simplest** test case of an
        **empty string** and move to **one & two numbers**
        """
        if len(number) < 1:
            if number == "":
                return 0
            else:
                return int(number)
        else:
            """
            allow \n to replace ','
            use regex with split to give list
            """

            pattern = r"[,:\n]"
            numbers = re.split(pattern, number)
            result = 0
            for i in numbers:
                result += int(i)
            return result
