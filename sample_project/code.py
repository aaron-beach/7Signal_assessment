def greeting():
    return "Hello, World!"


class StringCalculator:
    def add(number: str) -> int:
        if len(number) < 1:
            if number == "":
                return 0
            else:
                return int(number)
        else:
            numbers = number.split(",")
            result = 0
            for i in numbers:
                result += int(i)
            return result


"""
   1. The method can take 0, 1 or 2 numbers, and will
   return their sum (for an empty string it will return 0)
   for example
   `“” == 0 , “1” == 1 , “1,2” == 3`


   2. Start with the **simplest** test case of an **empty string** and move to **one & two numbers**


   3. Remember to solve things as **simply as possible** so that you force yourself to
   write tests you did not think about


   4. Remember to **refactor** after each passing test
"""
