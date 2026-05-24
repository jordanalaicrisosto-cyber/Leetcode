class Solution:
    def romanToInt(self, s: str) -> int:
        assert 1 <= len(s) <= 15

        number = 0
        dico_roman = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}

        if len(s) == 1 :
            return dico_roman[s[0]]
        i = 0
        while i < len(s) - 1 :
            assert s[i] in ('I', 'V', 'X', 'L', 'C', 'D', 'M')

            if dico_roman[s[i]] < dico_roman[s[i+1]] :
                number += dico_roman[s[i+1]] - dico_roman[s[i]]
                i+=2
            else :
                number += dico_roman[s[i]]
                i+=1

        if dico_roman[s[-1]] <= dico_roman[s[-2]] :
            number += dico_roman[s[-1]]

        assert 1 <= number <= 3999
        return number