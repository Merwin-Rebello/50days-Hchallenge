#Unique Number of Occurrences

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        nums = []
        occurences = []
        for num in arr:
            if num not in nums:
                occurence = arr.count(num)
                if occurence not in occurences:
                    occurences += [occurence]
                    nums += [num]
                else:
                    return False
        return True                