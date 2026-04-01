class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        nums.sort()
        streak_count = 1
        res = []

        for i in range(1, len(nums) + 1):
            if i == len(nums) or nums[i] != nums[i-1]:
                if streak_count > len(nums) / 3:
                    res.append(nums[i-1])
                streak_count = 1
            else:
                streak_count += 1
        return res