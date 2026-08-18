class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Frequency map list contains the frequency maps of all the visited unique strings 
        fmaplist = {}
        val = []
        value_updated = False
        counter = 0

        for i, string in enumerate(strs):
            freqmap = {}
            freqstr = ""

              
            for j, char in enumerate(string):
                freqmap[string[j]] = 1 + freqmap.get(char, 0)

            sorted_freqmap = dict(sorted(freqmap.items(), key=lambda item: item[0]))

                
            for index, (key, value) in enumerate(sorted_freqmap.items()):
                freqstr += key
                freqstr += str(value)

            if freqstr in fmaplist:
                index = fmaplist[freqstr]
                val[index].append(string)
            else:
                fmaplist[freqstr] = counter
                empty_list = []
                val.append(empty_list)
                val[counter].append(string)
                counter += 1

        return val