class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        copy = nums
        val = self.find(copy, target)
        i = val[0]
        j = val[1]
        ans = []
        for x in range(len(nums)):
            if (nums[x] == i):
                ans.append(x)
            elif (nums[x] == j):
                ans.append(x)

        return ans

    def find(self, nums: List[int], target: int):
        nums = sorted(nums)

        i, j = 0, len(nums)-1
        

        while (i<j):
            if(nums[i]+nums[j] == target):
                val = [nums[i], nums[j]]
                return val
            elif(nums[i]+nums[j] < target):
                i += 1
            elif(nums[i]+nums[j] > target):
                j -= 1

        val = [nums[i], nums[j]] 
        return val