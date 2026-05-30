from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == None :
            return ""

        if len(strs) == 1 :
            return strs[0]

        assert 1 <= len(strs) <= 200

        for i in range(len(strs)) :
            assert 0 <= len(strs[i]) <= 200
            strs[i] = list(strs[i])
            for c in range(len(list(strs[i]))) :
                assert 97 <= ord(strs[i][c]) <= 122

        str_com = ""
        strs.sort(key=len)
        ref = strs[0]
        c = 0
        print(strs)
        for i in range(1, len(strs)) :
            if ref[c] == strs[i][c] and i >= len(str_com) :
                str_com += strs[i][c]
                if c < len(ref) - 1 :
                    c += 1
                else :
                    return str_com
            if ref[c] != strs[i][c] :
                return ""

        return str_com
