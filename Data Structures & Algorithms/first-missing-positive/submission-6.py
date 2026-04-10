class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        min: 3
        [1,2,4]

        [1,2,4]
             i
        """

        numSet = set(nums)
        min_positive = float('inf')

        for i in range(1, len(nums) + 2):
            if i not in numSet:
                return i

        return min_positive