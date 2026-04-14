class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        pointer = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[pointer] = nums[i]
                pointer += 1


        return pointer
       
       
       
       
        # Fahd approach
        # visited = set()
        # write = 0
        # read = 0


        # while read < len(nums):

        #     # when the write is at duplicate number the read is looking for numbers 
        #     # that are not in visited and we're using the 'write' pointer to
        #     # to keep track of the last duplicate in the sorted sequence
        #     if nums[read] not in visited:
        #         nums[write] = nums[read]
        #         write += 1
        #         visited.add(nums[read]) 

        #     # setting write pointer to the next duplicate
        #     while write < len(nums) and nums[write] not in visited:
        #         visited.add(nums[write])
        #         write += 1

        #     read += 1
        
        # return write
        