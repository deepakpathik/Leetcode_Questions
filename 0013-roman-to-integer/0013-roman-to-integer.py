class Solution:
    def romanToInt(self, s):
        ans = 0
        index = 0
        while index < len(s):
            c = s[index]
            if c == 'I':
                if index + 1 < len(s):
                    if s[index + 1] == 'V':
                        ans += 4
                        index += 2
                    elif s[index + 1] == 'X':
                        ans += 9
                        index += 2
                    else:
                        ans += 1
                        index += 1
                else:
                    ans += 1
                    index += 1
            elif c == 'V':
                ans += 5
                index += 1
            elif c == 'X':
                if index + 1 < len(s):
                    if s[index + 1] == 'L':
                        ans += 40
                        index += 2
                    elif s[index + 1] == 'C':
                        ans += 90
                        index += 2
                    else:
                        ans += 10
                        index += 1
                else:
                    ans += 10
                    index += 1
            elif c == 'L':
                ans += 50
                index += 1
            elif c == 'C':
                if index + 1 < len(s):
                    if s[index + 1] == 'D':
                        ans += 400
                        index += 2
                    elif s[index + 1] == 'M':
                        ans += 900
                        index += 2
                    else:
                        ans += 100
                        index += 1
                else:
                    ans += 100
                    index += 1
            elif c == 'D':
                ans += 500
                index += 1
            elif c == 'M':
                ans += 1000
                index += 1
        return ans
