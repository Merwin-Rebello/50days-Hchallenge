#plus one 


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        plusone= int("".join([str(s) for s in digits]))+1
        return[int(s) for s in str(plusone)]