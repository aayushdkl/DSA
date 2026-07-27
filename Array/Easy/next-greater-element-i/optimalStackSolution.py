class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        
        # 1. Manually build the index map instead of using a dictionary comprehension
        nums1Idx = {}
        for i in range(len(nums1)):
            nums1Idx[nums1[i]] = i
            
        # 2. Manually build the result array instead of doing [-1] * len(nums1)
        res = []
        for i in range(len(nums1)):
            res.append(-1)
            
        stack = []
        
        # 3. Iterate through nums2 using explicit index loops
        for i in range(len(nums2)):
            cur = nums2[i]
            
            # Use len(stack) > 0 instead of the pythonic "while stack:"
            # Use stack[len(stack) - 1] to peek at the top instead of stack[-1]
            while len(stack) > 0 and cur > stack[len(stack) - 1]:
                val = stack.pop()
                idx = nums1Idx[val]
                res[idx] = cur
                
            # Check if the current value exists in our map keys
            if cur in nums1Idx:
                stack.append(cur)
                
        return res