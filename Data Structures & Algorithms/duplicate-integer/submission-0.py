class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if not nums:
            return False

    
        mySet = set()
        for n in nums:
            if n in mySet:
                return True
            else:
                mySet.add(n)
        return False