class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        target = 10, nums = [2,1,5,1,5,3]
                                       r
                                   l 
        """

        l = 0
        curSum = 0
        min_arr_len = float('inf')

        for r in range(len(nums)):
            curSum += nums[r]
            while l <= r and curSum >= target:
                min_arr_len = min((r - l + 1), min_arr_len)
                curSum -= nums[l]
                l += 1
            r += 1


        return min_arr_len if min_arr_len != float('inf') else 0
        