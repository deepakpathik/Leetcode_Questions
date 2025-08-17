class Solution:
    def longestCommonPrefix(self, strs):
        # Initialize with the first string
        prefix = strs[0]

        # Iterate over the rest of the strings
        for i in range(1, len(strs)):
            curr = strs[i]

            # Trim prefix if it's longer than current string
            if len(curr) < len(prefix):
                prefix = prefix[:len(curr)]

            # Compare characters to shrink prefix if mismatch
            for j in range(min(len(prefix), len(curr))):
                if curr[j] != prefix[j]:
                    prefix = prefix[:j]
                    break

        return prefix
