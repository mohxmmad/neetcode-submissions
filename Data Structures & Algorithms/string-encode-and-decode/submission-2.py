class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans += "~"
            ans += s
            ans += "~"
        return ans

    def decode(self, s: str) -> List[str]:
        val = []
        if len(s) != 0:
            current = ""
            appending = False
            for char in s:
                if char == "~" and appending == False:
                    appending = True
                elif char =="~" and appending == True:
                    appending = False
                    val.append(current)
                    current = ""
                else:
                    current += char
                    
        else:
            val = []
        return val