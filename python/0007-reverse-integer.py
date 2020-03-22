from typing import List, TypeVar
import math

class Solution:
    def reverse(self, x: int) -> int:
        is_minus = False
        if x < 0:
            x = -x
            is_minus = True


        INT_MAX = 2147483647
        INT_MIN = -2147483648
        rev = 0

        while x != 0:
            pop = x % 10
            x /= 10
            x = math.floor(x)

            if (rev > INT_MAX/10 or (rev == INT_MAX / 10 and pop > 7)):
                return 0
            if (rev < INT_MIN/10 or (rev == INT_MIN / 10 and pop < -8)):
                return 0
            rev = rev * 10 + pop

        if is_minus:
            rev = -rev

        return rev


solution = Solution()
print(solution.reverse(-123))
