class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        num1Idx = {}
        n1=len(nums1)
        n2= len(nums2)
        for i in range(0,n1):
            num1Idx[nums1[i]]=i
        res = [-1]*(n1)
        stack = []

        for i in range(0,n2):
            currentValue = nums2[i]

            while stack and currentValue > stack[-1]:
                poppedValue = stack.pop()
                index = num1Idx[poppedValue]
                res[index]=currentValue
            if currentValue in num1Idx:
                stack.append(currentValue)

        return res