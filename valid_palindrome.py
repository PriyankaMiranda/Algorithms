class Solution:
    def validPalindrome(self, s: str) -> bool:
        def perfect_palindrome(s):
            i = 0 
            j = len(s) - 1
            while i < j:
                if (s[i] != s[j]):
                    return False
                i += 1
                j -= 1
            return True


    
        i = 0 
        j = len(s) - 1
        while i < j: 
            if s[i] != s[j]:
                return perfect_palindrome(s[:i] + s[i+1:]) or perfect_palindrome(s[:j] + s[j+1:])
            i += 1
            j -= 1
        return True



