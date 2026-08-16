class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        for char in s:
            try: 
                map[char] += 1
            except:
                map[char] = 1

        for char in t:
            try:
                map[char] -= 1
            except:
                return False

        for value in map:
            if map[value] != 0:
                return False
        
        return True