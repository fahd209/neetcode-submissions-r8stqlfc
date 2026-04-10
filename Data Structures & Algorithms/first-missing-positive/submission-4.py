class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        min: 3
        [1,2,4]

        [1,2,4]
             i
        """

        numSet = set(nums)
        max_num = max(nums)
        min_positive = float('inf')

        if max_num < 0:
            return 1

        for i in range(max_num + 2):
            if i != 0 and i not in numSet:
                min_positive = min(min_positive, i)

        return min_positive