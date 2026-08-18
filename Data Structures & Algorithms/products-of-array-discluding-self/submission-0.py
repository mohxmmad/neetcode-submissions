class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        output= []
        iz = []
        for i in range(len(nums)):
            if nums[i] == 0:
                iz.append(i)
            else:
                product = nums[i] * product

        for i in range(len(nums)):
            if len(iz) > 0:
                if len(iz) > 1:
                    output.append(0)
                else:
                    if i == iz[0]:
                        output.append(product)
                    else:
                        output.append(0)
            else:
                output.append(int(product/nums[i]))
            
        return output