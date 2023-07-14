
#  third maximum number
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        group= list(set(nums))
        if len(group)>=3:
            group.sort(reverse=True)
            return group[2]
        else:
            return max(group)