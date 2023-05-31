class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)#direct there is a remove function in python which helps to remove the 
            #dedicated value and return the remaiining values in the list
            