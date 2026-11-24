class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for i,num in enumerate(nums):
            A = target - num
            if A  in result:
                return [result[A],i]
            result[num] = i

        
        

   