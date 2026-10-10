class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:

            if n in seen:
                return False

            seen.add(n)

            digit_square_sum = 0

            while n > 0:
                digit = n % 10
                digit_square_sum += digit * digit
                n = n // 10

            n = digit_square_sum

        return True
        