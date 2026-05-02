
#Brute way
class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        i = 0
        n = len(s)

        while i < n:
            # Skip spaces
            while i < n and s[i] == " ":
                i += 1

            word = ""
            # Collect characters of a word
            while i < n and s[i] != " ":
                word += s[i]
                i += 1

            if word:
                words.append(word)

        words.reverse()
        return " ".join(words)

#OPTIMAL
