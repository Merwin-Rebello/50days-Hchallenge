#Check if The Number is Fascinating

class Solution:
    def isFascinating(self, n: int) -> bool:
        concatination = str(n) + str(2*n) + str(3*n)
        if '0' in concatination:
            return False
        if len(concatination)>9:
            return False
        for i in range (1,10):
            if str(i) not in concatination:
                return False
        return True        