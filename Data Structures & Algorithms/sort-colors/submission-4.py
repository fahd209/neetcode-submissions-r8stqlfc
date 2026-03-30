class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


        i = 0
        l = 0
        r = len(nums) - 1

        while i <= r:
            if nums[i] == 0:
                temp = nums[l]
                nums[l] = nums[i]
                nums[i] = temp
                l += 1
                i += 1
            elif nums[i] == 2:
                temp = nums[r]
                nums[r] = nums[i]
                nums[i] = temp
                r -= 1
            else:
                i += 1

        # if len()

        # group colors
        # color_count = [0] * 3
        # for n in nums:
        #     color_count[n] += 1
        
        # # loop through each group and replace the elements in num with the elements in the group
        # # print(color_group)
        # index = 0
        # for i in range(3):
        #     for _ in range(color_count[i]):
        #         nums[index] = i
        #         index += 1