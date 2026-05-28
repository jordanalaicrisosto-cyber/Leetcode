class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        assert 1 <= len(s) <= 10**4

        s_clean = ""

        for c in s :
            assert 65 <= ord(c) <= 90 or 97 <= ord(c) <= 122 or c == " "

        i = 0
        while s[i] == ' ' :
            i+=1

        j = len(s) - 1
        while s[j] == ' ' :
            j-=1

        s_clean = s[i : j+1]

        list_words = s_clean.split(" ")
        print(list_words)
        assert list_words != []

        return len(list_words[-1])
