class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        understanding:
            array: nums 
            integer: target

            return i and j  where nums[i] + nums[j] == target
            every input will have an output of i and j

        approach:
            prev = {
                4:0, 5:1, 
            }

            [4,5,6], 10
                 i
        """

        prev = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in prev:
                return [prev[diff], i]
            else:
                prev[nums[i]] = i
