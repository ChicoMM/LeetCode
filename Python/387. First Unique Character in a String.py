class Solution(object):
    def firstUniqChar(self, s):
        c ={}
        for ind, ch in enumerate(s):
            if ch not in c:
                c[ch] = [ind,1]
            else:
                c[ch][1] +=1
        for ch, val in c.items():
            if val[1] == 1:
                return val[0]
        return -1



        