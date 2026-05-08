class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in range(0,len(nums1)):
            for j in range(0,len(nums2)):
                if nums1[i]==nums2[j] and nums1[i] not in res:
                    res.append(nums1[i])
        return res