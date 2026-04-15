class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        visited = set()
        result = []
        nums.sort()


        for a in range(len(nums)):
            for b in range(a + 1, len(nums)):
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
                        if tuple(sum_array) not in visited:
                            result.append(sum_array)
                            visited.add(tuple(sum_array))
                        else:
                            c += 1
                            d -= 1

        return result

