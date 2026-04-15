class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        # visited = set()
        result = []
        nums.sort()


        for a in range(len(nums)):
            if a > 0 and nums[a-1] == nums[a]:
                continue 

            for b in range(a + 1, len(nums)):

                if b > a + 1 and nums[b - 1] == nums[b]:
                    continue

                c = b + 1
                d = len(nums) - 1
                while c < d:
                    sum = nums[a] + nums[b] + nums[c] + nums[d]
                    if sum > target:
                        d -= 1
                    elif sum < target:
                        c += 1
                    else:
                        sum_array = [nums[a], nums[b], nums[c], nums[d]]
                        result.append(sum_array)
                        c += 1
                        d -= 1
                        
                        while nums[c-1] == nums[c] and c < d:
                            c += 1

        return result

