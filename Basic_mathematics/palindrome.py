
#most optimal

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # negatives and numbers ending with 0 (except 0 itself) are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x //= 10

        # for even digits: x == rev
        # for odd digits: x == rev // 10 (middle digit ignored)
        return x == rev or x == rev // 10
