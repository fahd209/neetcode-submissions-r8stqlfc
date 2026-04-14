class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        visited = set()
        write = 0
        read = 0

        while read < len(nums):

            if nums[read] not in visited:
                nums[write] = nums[read]
                write += 1
                visited.add(nums[read]) 

            
            while write < len(nums) and nums[write] not in visited:
                visited.add(nums[write])
                write += 1

            read += 1

        
        return write
        