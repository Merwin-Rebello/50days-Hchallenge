# insert position and also if not present add the number 
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
         if (target <= nums[i]):# lessthanequal to because we also want if we want to insert the element where we would insert it and as it is sorted so we get the position
             return i
        return len(nums)    