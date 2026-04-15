class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-4, -1,-1,0, 1,2]
                #    i j  k

        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            if nums[i] > 0:
                return result

            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    j += 1
                    while nums[j-1] == nums[j] and j < k:
                        j += 1 
                elif sum > 0:
                    k -= 1
                else:
                    j += 1

        return result