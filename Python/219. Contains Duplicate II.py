class Solution:
    def containsNearbyDuplicate(self, nums, k) -> bool:
        right = 0
        left = 0
        d = {}
        while right-left <= min(k,len(nums)-1):
            if nums[right] not in d:
                d[nums[right]] = 1
            else:
                return True
            right +=1
        while right < len(nums):
            del d[nums[left]]
            if nums[right] not in d:
                d[nums[right]] = 1
            else:
                return True
            right+=1
            left+=1
        return False
            



        

