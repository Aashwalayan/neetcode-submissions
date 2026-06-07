class Solution:

    def encode(self, strs: List[str]) -> str:
        
        
        encodedStr = ""

        for i in range(len(strs)):
            encodedStr += str(len(strs[i]))
            encodedStr += "#" + strs[i]
        
        return encodedStr

    #"  4#cate5#he#lo  "

    def decode(self, s: str) -> List[str]:

        strs = []
        length = 0
        i = 0
        j = 0

        while i < len(s):    
            
            while s[j] != '#':
                j += 1

            length = int(s[i : j])

            word = s[j + 1 : j + 1 + length]
            strs.append(word)

            nextPos = j + 1 + length
            i = nextPos
            j = nextPos

        return strs

            
            