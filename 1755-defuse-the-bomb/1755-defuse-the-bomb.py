class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0] * n

        if k == 0:
            return res
        
        for i in range(n):
            total = 0
            if k > 0:
                for j in range(1, k + 1):
                    total += code[(i + j) % n]
            else:  # k < 0
                for j in range(1, -k + 1):
                    total += code[(i - j + n) % n]
            res[i] = total
        
        return res