class Solution(object):
    def maximumLengthSubstring(self, s):
        l = 0
        r = 0
        maxi = 1
        counter = {}
        counter[s[0]] = 1
        while r < len(s)-1:
            r+=1
            if counter.get(s[r]):
                counter[s[r]] +=1
            else:
                counter[s[r]] = 1
            while counter[s[r]] == 3:
                counter[s[l]] -=1
                l+=1
            maxi = max(maxi, r-l+1)
        return maxi