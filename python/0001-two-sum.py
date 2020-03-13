from typing import List, TypeVar

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]

        
solution = Solution()
print(solution.twoSum([2,7,11,15],9))

