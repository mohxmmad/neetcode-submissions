class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        nums = sorted(nums)

        i,j = 0, 1

        while j<len(nums):
            if(nums[i] == nums[j]):
                return True
            
            else:
                i = j
                j += 1
        
        return False
