class Solution:
    def twoSum(self, nums, target):
        d = {}
        for idx, num in enumerate(nums):
            dif = target - num
            if dif not in d:
                d[nums[idx]] = idx
            else:
                return [d[dif],idx]

        