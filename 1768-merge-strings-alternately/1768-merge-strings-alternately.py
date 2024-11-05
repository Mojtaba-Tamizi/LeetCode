class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        output = ''
        if len(word1) >= len(word2):
            min_len = len(word2)
            last_word = word1[min_len:]
        else:
            min_len = len(word1)
            last_word = word2[min_len:]
        while i < min_len:
            output += word1[i] + word2[i]
            i += 1
        if i < len(word2) or i < len(word1):
            output += last_word
            
        return output