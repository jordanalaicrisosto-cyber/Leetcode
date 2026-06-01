from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == None :
            return ""

        if len(strs) == 1 :
            return strs[0]

        assert 1 <= len(strs) <= 200

        strs.sort(key=len)
        strs.reverse()
        strs_col = [['é' for _ in range(len(strs))] for _ in range(len(strs[0]))]

        for i in range(len(strs)) :
            assert 0 <= len(strs[i]) <= 200
            for c in range(len(list(strs[i]))) :
                assert 97 <= ord(strs[i][c]) <= 122
                strs_col[c][i] = strs[i][c]

        str_com = ""
        flag = True
        for c in range(len(strs_col)) :
            for r in range(len(strs_col[c])-1) :
                if strs_col[c][r] != strs_col[c][r+1] :
                    flag = False
            if flag :
                str_com += strs_col[c][0]
            else :
                break

        return str_com
