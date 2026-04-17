class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # reverse the array
        k = k % len(nums)

        if k == 0:
            return nums

        def reverse(L, R):
            while L < R:
                temp = nums[L]
                nums[L] = nums[R]
                nums[R] = temp 
                L += 1
                R -= 1

        reverse(0, len(nums) - 1)
        reverse(0, k - 1)
        reverse(k, len(nums) - 1)
        
    


            