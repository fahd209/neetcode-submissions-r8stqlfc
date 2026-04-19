class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        j = 0
        i = 0

        visited = set()

        while j < len(nums):

            if (j - i) > k:
                visited.remove(nums[i])
                i += 1
                
            if nums[j] in visited:
                return True
            
            visited.add(nums[j])
            j += 1

        return False