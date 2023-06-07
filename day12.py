# single number out of the array find hte one which is not repeated at alld
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict = {}  
  
        for i in nums:
            if i not in dict:  
                dict[i] = True  
            else:
                dict[i] = False  

        for k,v in dict.items():
            if v == True:  
                return k 