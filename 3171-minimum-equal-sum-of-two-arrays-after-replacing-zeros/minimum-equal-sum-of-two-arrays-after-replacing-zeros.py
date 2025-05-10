class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2, z1, z2 = sum(nums1), sum(nums2), nums1.count(0), nums2.count(0)
        return -(z1==0 and s1<s2+z2 or z2==0 and s1+z1>s2) or max(s1+z1,s2+z2)