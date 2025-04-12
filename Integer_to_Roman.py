from unittest import removeResult


class Solution:
    def intToRoman(self, num: int) -> str:
        # list of possible maps in ascending order
        symbolList = [
            ["M", 1000], ["CM", 900], ["D", 500], ["CD", 400],
            ["C", 100], ["XC", 90], ["L", 50], ["XL", 40],
            ["X", 10], ["IX", 9], ["V", 5], ["IV", 4], ["I", 1]]

        # Iterate result in descending order since it is largest to smallest
        result = ""

        for symbol, val in symbolList:
            if num // val:
                count = num // val # how many times does val goes into num
                result += (symbol * count) # multiply the count to how many symbols then add it to the result

                num = num % val # chop off the first place value and use the remainder and update num

        return result






