class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre_product = [0] * n 
        post_product = [0] * n
        res = [0] * n

        prod1 = 1
        prod2 = 1

        for i in range(n):
            pre_product[i] = prod1
            prod1 *= nums[i]
        
        for i in range(n - 1, -1, -1):
            # print(i)
            post_product[i] = prod2
            prod2 *= nums[i] 

        print(pre_product)
        print(post_product)

        for i in range(n):
            res[i] = pre_product[i] * post_product[i]

        return res