class Solution:
    def twoSum(self, nums:List[int], target:int)->List[int]:
        a=[]
        for i in range(len(nums)):# i will iterate from 0 to length-1
            for j in range(i+1,len(nums)):# j will iterate form 1  to length 
                if (nums[i]+nums[j]== target):# adding the first and the second element of thesame array
                    a.append(i) #appending both the the  indexeses
                    a.append(j)
                    break
                else:
                    continue
        return a   