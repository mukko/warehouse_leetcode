from typing import List, TypeVar
import math

# version type change. slow than org
class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2147483647
        INT_MIN = -2147483648

        is_minus = False
        if x < 0:
            x = -x
            is_minus = True

        org_str = str(x)

        rev_str = org_str[::-1] 

        rev = int(rev_str)

        if rev > INT_MAX:
            return 0

        if rev < INT_MIN:
            return 0

        if is_minus:
            rev = -rev

        return rev


solution = Solution()
print(solution.reverse(-123))
