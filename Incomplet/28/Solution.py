class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if len(haystack) < len(needle) :
            return - 1

        assert 1 <= len(haystack) and len(needle) <= 10**4

        start = -1
        isStart = False
        indl = 0
        ih = 0

        for i in range(len(haystack)) :
            assert 97 <= ord(haystack[i]) <= 122

        while indl < len(needle) and ih < len(haystack):
            assert 97 <= ord(needle[indl]) <= 122
            print(needle[indl], haystack[ih])
            if needle[indl] == haystack[ih] :
                if not(isStart) :
                    isStart = True
                    start = ih
                indl += 1
            elif needle[indl] != haystack[ih] :
                isStart = False
                start = -1
                indl = 0
            ih += 1

        return start
