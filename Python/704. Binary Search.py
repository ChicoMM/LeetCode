class Solution(object):
    def search(self, nums, n):
        lo = 0
        hi = len(nums)
        steps = 0
        found = False
        while lo < hi:
            steps+=1
            mid = int((lo+hi)/2)
            if nums[mid] == n:
                return mid
            elif nums[mid] < n:
                lo = mid+1
            else:
                hi = mid
        return -1
        