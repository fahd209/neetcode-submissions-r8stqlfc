class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        visited = set()
        write = 0
        read = 0


        while read < len(nums):

            # when the write is at duplicate the read is looking for numbers 
            # that are not in visited and we're using the 'write' pointer to
            # 
            if nums[read] not in visited:
                nums[write] = nums[read]
                write += 1
                visited.add(nums[read]) 

            # setting write pointer to the next duplicate
            while write < len(nums) and nums[write] not in visited:
                visited.add(nums[write])
                write += 1

            if write > read:
                read = write + 1
            else:
                read += 1
        
        return write
        