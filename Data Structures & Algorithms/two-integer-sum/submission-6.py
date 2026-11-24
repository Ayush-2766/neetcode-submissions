class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            
            A = target - num 
            if A in seen:
                return [seen[A], i]
            seen[num] = i
        

   