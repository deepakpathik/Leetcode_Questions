class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        val = 0
        symbs = {'I':1, "V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for i in range(len(s)-1):
            if symbs[s[i]] < symbs[s[i+1]]:
                val -= symbs[s[i]]
            else:
                val += symbs[s[i]]

        return val + symbs[s[-1]]

        
        # symbs = {'I':1, "V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        # val = 0

        # for curr, nxt in zip(s, s[1:]):
        #     if symbs[curr] < symbs[nxt]:
        #         val -= symbs[curr]
        #     else:
        #         val += symbs[curr]

        # val += symbs[s[-1]]
        # return val