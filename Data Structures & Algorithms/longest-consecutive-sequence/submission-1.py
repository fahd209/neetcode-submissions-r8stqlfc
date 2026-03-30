class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)
        longest_seq = 0

        # loop through each num and check if its a start of sequence
        for n in nums:
            if not n - 1 in nums_set:
                current_sequence = 1
                
                # keep incrementing the current_sequence counter until we break out the current sequence
                while n + current_sequence in nums_set:
                    current_sequence += 1
                longest_seq = max(longest_seq, current_sequence)

        return longest_seq
