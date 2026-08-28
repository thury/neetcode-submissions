class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        pref = [1]
        suf = [1]
        for prefIndex in range(0, len(nums)-1):
            pref.append(pref[-1]*nums[prefIndex])
            suf.insert(0, suf[0]*nums[len(nums) - prefIndex - 1])
        for resIndex in range(len(nums)):
            res.append(pref[resIndex] * suf[resIndex])
        return res 