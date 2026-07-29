from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = {}
        s2Count = {}

        for c in s1:
            s1Count[c] = s1Count.get(c, 0) + 1

        # first window
        for i in range(len(s1)):
            s2Count[s2[i]] = s2Count.get(s2[i], 0) + 1

        if s1Count == s2Count:
            return True

        left = 0

        for right in range(len(s1), len(s2)):
            s2Count[s2[right]] = s2Count.get(s2[right], 0) + 1
            removeChar = s2[left]
            s2Count[removeChar] -= 1

            if s2Count[removeChar] == 0:
                del s2Count[removeChar]

            left += 1

            if s1Count == s2Count:
                return True
        return False

