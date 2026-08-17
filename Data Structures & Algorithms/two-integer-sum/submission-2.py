class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                val = [hashmap[diff], i]
                return val
            else:
                hashmap[n] = i
        val = [0 ,0]
        return val
