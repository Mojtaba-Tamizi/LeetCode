class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        output = ""
        if len(str1) == 0 or len(str2) == 0:
            return output
        
        for i in range(len(str1)):
            if len(str2) % (i + 1) == 0 and len(str1) % (i + 1) == 0:
                string = str1[:i+1]
                s1 = string * (len(str1) // (i + 1))
                s2 = string * (len(str2) // (i + 1)) 
                if s1 == str1 and s2 == str2:
                    output = string
        return output