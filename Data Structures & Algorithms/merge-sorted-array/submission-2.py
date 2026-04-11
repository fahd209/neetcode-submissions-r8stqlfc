class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        high level explanation of the approach

        since both arrays are sorted we can have a pointer at each valid greatest element in each array 
        and we can have a pointer at the last element in nums1

        we then compare the two greatest elements in both arrays, the element thats greater will go to
        nums1[last] then we can decrement last and the pointer for the array item that was set to be at nums[last]

        """
        last = m + n - 1
        j = len(nums2) - 1
        i = m - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[last] = nums1[i]
                last -= 1
                i -= 1
            else:
                nums1[last] = nums2[j]
                last -= 1
                j -= 1