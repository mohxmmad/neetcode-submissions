class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = set()
        if len(nums) <= 0:
            return 0
        elif len(nums) == 1:
            return 1
        else:
            
            unique_nums = set()
            for i in range(len(nums)):
                if nums[i] in unique_nums:
                    continue
                else:
                    unique_nums.add(nums[i])
            nums = list(unique_nums)
            nums = sorted(nums)
            counter = 0
            for i in range(1, len(nums)):
                if nums[i] - nums[i-1] == 1 or nums[i] - nums[i-1] == -1:
                    counter += 1
                    if i == len(nums)-1:
                        counter += 1
                        hashmap.add(counter)
                        counter = 0
                else:
                    if counter > 0:
                        counter += 1
                        hashmap.add(counter)
                        counter = 0
        
        max = 1
        for value in hashmap:
            if value > max:
                max = value

        return max