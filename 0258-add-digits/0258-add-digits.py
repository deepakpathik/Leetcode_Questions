class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10 and num >= 0:
            return num
        # if num == 0:
            # return 0 
        else:
            return 1+(num-1)%9