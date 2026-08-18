class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqmap = {}
        for x in nums:
            freqmap[x] = 1 + freqmap.get(x, 0)
        sorted_freqmap = dict(sorted(freqmap.items(), key=lambda item: item[1]))

        i = len(sorted_freqmap) - 1
        val = []
        freq = list(sorted_freqmap.keys())
        while (k > 0):
            val.append(freq[i])
            k -= 1
            i -= 1
        return val