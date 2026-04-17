class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # reverse the array
        L = 0
        R = len(nums) - 1
        k = k % len(nums)
        while L < R:
            temp = nums[L]
            nums[L] = nums[R]
            nums[R] = temp 
            L += 1
            R -= 1

        L = 0
        R = k - 1
        while L < R:
            temp = nums[L]
            nums[L] = nums[R]
            nums[R] = temp 
            L += 1
            R -= 1

        L = k
        R = len(nums) - 1
        while L < R:
            temp = nums[L]
            nums[L] = nums[R]
            nums[R] = temp 
            L += 1
            R -= 1


            